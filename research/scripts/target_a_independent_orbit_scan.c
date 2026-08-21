/* Independent full-space dihedral-orbit scanner for Target A.

   This checker deliberately does not share canonicalization, necklace
   generation, traversal order, or data structures with target_a_bracelets.py.
   It scans every integer word, constructs each orbit directly, and consumes
   the corresponding entry in a disk-mapped table produced by the FKM route.
*/

#define _POSIX_C_SOURCE 200809L

#include <errno.h>
#include <fcntl.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

static uint64_t rotate_left_n(uint64_t word, unsigned shift, unsigned n) {
    const uint64_t mask = (UINT64_C(1) << n) - 1;
    shift %= n;
    if (shift == 0) {
        return word & mask;
    }
    return ((word << shift) | (word >> (n - shift))) & mask;
}

static uint64_t reverse_n(uint64_t word, unsigned n) {
    uint64_t reversed = 0;
    for (unsigned i = 0; i < n; ++i) {
        reversed = (reversed << 1) | (word & 1U);
        word >>= 1;
    }
    return reversed;
}

static int seen(const uint8_t *bits, uint64_t word) {
    return (bits[word >> 3] >> (word & 7U)) & 1U;
}

static void mark(uint8_t *bits, uint64_t word) {
    bits[word >> 3] |= (uint8_t)(1U << (word & 7U));
}

static int append_unique(uint64_t *orbit, unsigned *size, uint64_t word) {
    for (unsigned i = 0; i < *size; ++i) {
        if (orbit[i] == word) {
            return 0;
        }
    }
    orbit[(*size)++] = word;
    return 1;
}

int main(int argc, char **argv) {
    if (argc != 3 && argc != 4) {
        fprintf(stderr, "usage: %s N PRIMARY_TABLE [INDEPENDENT_RECORDS]\n", argv[0]);
        return 2;
    }

    char *end = NULL;
    const unsigned long parsed_n = strtoul(argv[1], &end, 10);
    if (*argv[1] == '\0' || *end != '\0' || parsed_n < 8 || parsed_n > 30 ||
        (parsed_n & 1U) != 0) {
        fprintf(stderr, "N must be an even integer in [8,30]\n");
        return 2;
    }
    const unsigned n = (unsigned)parsed_n;
    const uint64_t universe = UINT64_C(1) << n;
    const size_t visited_bytes = (size_t)((universe + 7) / 8);

    const int fd = open(argv[2], O_RDWR);
    if (fd < 0) {
        fprintf(stderr, "open failed: %s\n", strerror(errno));
        return 2;
    }
    struct stat stat_buffer;
    if (fstat(fd, &stat_buffer) != 0 || (uint64_t)stat_buffer.st_size != universe) {
        fprintf(stderr, "primary table size mismatch\n");
        close(fd);
        return 2;
    }
    uint8_t *primary = mmap(NULL, (size_t)universe, PROT_READ | PROT_WRITE,
                            MAP_SHARED, fd, 0);
    if (primary == MAP_FAILED) {
        fprintf(stderr, "mmap failed: %s\n", strerror(errno));
        close(fd);
        return 2;
    }
    uint8_t *visited = calloc(visited_bytes, 1);
    if (visited == NULL) {
        fprintf(stderr, "visited allocation failed\n");
        munmap(primary, (size_t)universe);
        close(fd);
        return 2;
    }
    FILE *records = NULL;
    if (argc == 4) {
        records = fopen(argv[3], "wb");
        if (records == NULL) {
            fprintf(stderr, "record output open failed: %s\n", strerror(errno));
            free(visited);
            munmap(primary, (size_t)universe);
            close(fd);
            return 2;
        }
    }

    uint64_t legal_words = 0;
    uint64_t representatives = 0;
    uint64_t consumed = 0;
    uint64_t represented = 0;
    uint64_t missing = 0;
    uint64_t orbit_mismatches = 0;
    uint64_t canonicality_failures = 0;
    uint64_t orbit_histogram[61] = {0};
    uint64_t defect_histogram[31] = {0};

    for (uint64_t word = 0; word < universe; ++word) {
        const unsigned defects = (unsigned)__builtin_popcountll(word);
        if (defects & 1U) {
            continue;
        }
        ++legal_words;
        if (seen(visited, word)) {
            continue;
        }

        uint64_t orbit[60];
        unsigned orbit_size = 0;
        const uint64_t reflected = reverse_n(word, n);
        for (unsigned shift = 0; shift < n; ++shift) {
            append_unique(orbit, &orbit_size, rotate_left_n(word, shift, n));
            append_unique(orbit, &orbit_size, rotate_left_n(reflected, shift, n));
        }
        uint64_t minimum = orbit[0];
        for (unsigned i = 0; i < orbit_size; ++i) {
            if (orbit[i] < minimum) {
                minimum = orbit[i];
            }
            mark(visited, orbit[i]);
        }
        if (minimum != word) {
            ++canonicality_failures;
        }

        ++representatives;
        represented += orbit_size;
        if (records != NULL) {
            const uint8_t compact_orbit_size = (uint8_t)orbit_size;
            if (fwrite(&word, sizeof(word), 1, records) != 1 ||
                fwrite(&compact_orbit_size, sizeof(compact_orbit_size), 1, records) != 1) {
                fprintf(stderr, "record output write failed: %s\n", strerror(errno));
                fclose(records);
                free(visited);
                munmap(primary, (size_t)universe);
                close(fd);
                return 2;
            }
        }
        ++defect_histogram[defects];
        ++orbit_histogram[orbit_size];
        if (primary[word] == 0) {
            ++missing;
            if (missing <= 8) {
                fprintf(stderr, "missing primary record: word=%" PRIu64 " orbit=%u\n",
                        word, orbit_size);
            }
        } else {
            ++consumed;
            if (primary[word] != orbit_size) {
                ++orbit_mismatches;
                if (orbit_mismatches <= 8) {
                    fprintf(stderr,
                            "orbit mismatch: word=%" PRIu64 " primary=%u independent=%u\n",
                            word, primary[word], orbit_size);
                }
            }
            primary[word] = 0;
        }
    }

    const int pass = legal_words == (UINT64_C(1) << (n - 1)) &&
                     represented == (UINT64_C(1) << (n - 1)) &&
                     missing == 0 && orbit_mismatches == 0 &&
                     canonicality_failures == 0;

    printf("{\n");
    printf("  \"status\": \"%s\",\n", pass ? "PASS" : "FAIL");
    printf("  \"n\": %u,\n", n);
    printf("  \"universe_words\": %" PRIu64 ",\n", universe);
    printf("  \"legal_q_words\": %" PRIu64 ",\n", legal_words);
    printf("  \"independent_representatives\": %" PRIu64 ",\n", representatives);
    printf("  \"consumed_primary_records\": %" PRIu64 ",\n", consumed);
    printf("  \"represented_q_vectors\": %" PRIu64 ",\n", represented);
    printf("  \"missing_primary_records\": %" PRIu64 ",\n", missing);
    printf("  \"orbit_size_mismatches\": %" PRIu64 ",\n", orbit_mismatches);
    printf("  \"canonicality_failures\": %" PRIu64 ",\n", canonicality_failures);
    printf("  \"defect_count_histogram\": {");
    int first = 1;
    for (unsigned i = 0; i <= n; ++i) {
        if (defect_histogram[i] == 0) continue;
        printf("%s\"%u\": %" PRIu64, first ? "" : ", ", i, defect_histogram[i]);
        first = 0;
    }
    printf("},\n  \"orbit_size_histogram\": {");
    first = 1;
    for (unsigned i = 1; i <= 2 * n; ++i) {
        if (orbit_histogram[i] == 0) continue;
        printf("%s\"%u\": %" PRIu64, first ? "" : ", ", i, orbit_histogram[i]);
        first = 0;
    }
    printf("}\n}\n");

    msync(primary, (size_t)universe, MS_SYNC);
    if (records != NULL && fclose(records) != 0) {
        fprintf(stderr, "record output close failed: %s\n", strerror(errno));
        free(visited);
        munmap(primary, (size_t)universe);
        close(fd);
        return 2;
    }
    free(visited);
    munmap(primary, (size_t)universe);
    close(fd);
    return pass ? 0 : 1;
}
