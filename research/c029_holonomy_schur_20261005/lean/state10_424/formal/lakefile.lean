import Lake

open Lake DSL

package TargetA where
  srcDir := "."

@[default_target]
lean_lib TargetA

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "v4.33.1"
