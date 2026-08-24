# Formal Manuscript Freeze Record

## Reference checkpoint

```text
branch: agent/target-a-discovery-snapshot
HEAD at Task 57 start: e6a01d8bf30088dae1042a237398bee2df138280
```

## Frozen trees

```text
English: research/paper/manuscript_tex_pub
tree:    59e3a8f73a152ef06f994e979b7219a3365efeae

Chinese: research/paper/manuscript_tex_pub_zh
tree:    57ae03fb5b90866f84d0d72b414008678e8f5004
```

Both tree hashes were recomputed from the reference checkpoint. Neither
directory has a tracked diff. Task 57 proof-completion files live outside both
formal manuscript trees.

The Task 57.5 Lane D consistency repair starts from
`06316943472d9a1ea22f57b383bd3a0091cd4577` and retains the same two tree
hashes. Its allowed edit set excludes both manuscript directories.

## Git policy

This proof-completion pass does not create or switch a branch or worktree and
does not commit, push, or open a pull request. Historical research files are
not rewritten.
