# Exact finite Hall-profile baseline

Convention: M2=K2; M_(k+1)=μ(M_k). For each nonempty subset S, compute the independence number of the induced graph with

α(S)=max(α(S−v),1+α(S−N[v])), α(empty)=0,

where v is the least set bit. Both masks on the right are smaller than S, so increasing-mask dynamic programming is exact. For each a, maximize |S| over masks with α(S)=a. Their ratios give the Hall ratio.

Executed 5 October 2026:

g++ -O2 -std=c++17 mycielski_profile.cpp -o mycielski_profile
./mycielski_profile

Results: h(M2)=2; h(M3)=5/2; h(M4)=8/3; h(M5)=3. The M5 execution covers all 2^23−1=8,388,607 nonempty subsets. Its profile is

q5(1..11)=(2,5,8,12,15,18,19,20,21,22,23).

At ratio three, maximum-order witnesses have (|S|,α(S))=(12,4),(15,5),(18,6). Their respective counts are 220,175,5. Counts refer to labelled subsets, not isomorphism orbits. Witness bitmasks are in mycielski_profile.txt; vertex labelling is exactly the iterative original/shadow/apex order in the source.

This is a freshly executed finite baseline. No publication novelty is claimed, no extrapolation to M6 or all k is made, and no Lean compilation was performed. The w-function reformulation predates this computation: Barnett's 2016 dissertation, Definition2.1.1 and Chapter4.
