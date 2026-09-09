import Lake

open Lake DSL

package AMLStabilization where
  srcDir := "."

@[default_target]
lean_lib AMLStabilization

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.33.1"
