# Task 60 Exceptional Displacement Collisions

Before reduction modulo `N`, the nonzero displacement labels in `H_s` are

```text
+/-2, +/-2s, +/-(s-1), +/-(s+1).
```

## Generic fixed-`s` collision

For integer displacements, the only collision in the regime `s>=2` is

```text
s=3:  2=s-1.
```

Thus the `+2` coefficient is the sum of the pure step-one contribution and
the `+(s-1)` mixed contribution; the negative channel behaves similarly.

## Complete modular collision list

Because every positive magnitude above is less than `N`, any additional
collision is either equality, complementarity `d+e=N`, or self-opposition
`2d=N`. Under `2<=s<N/2`, the complete additional list is:

| Condition | Collision |
|---|---|
| `N=2s+2` | `+2=-2s`, `-2=+2s`, and `+(s+1)=-(s+1)` modulo `N` |
| `N=3s-1` | `+2s=-(s-1)` and `-2s=+(s-1)` |
| `N=3s+1` | `+2s=-(s+1)` and `-2s=+(s+1)` |
| `N=4s` | `+2s=-2s` |
| `(N,s)=(5,2)` | `+2=-(s+1)` and its negative counterpart |

Some conditions overlap: `(5,2)` also lies on `N=3s-1`, and `(8,3)` combines
the generic `s=3` collision with `N=2s+2` and `N=3s-1`.

No listed collision invalidates the path-sum formula. It invalidates only a
presentation that treats the channels as distinct matrix entries.
