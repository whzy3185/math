import Lake

open Lake DSL

package TargetA where
  srcDir := "."

@[default_target]
lean_lib TargetA

require mathlib from git
  "https://mirror.sjtu.edu.cn/git/lean4-packages/mathlib4" @ "v4.33.1"
