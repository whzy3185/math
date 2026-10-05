// Independent exact counterexample search after the exterior-private-pair reduction.
// All same/opposite residual placements at gamma=2,3 are covered.
#include <vector>
#include <utility>
#include <iostream>
#include <cassert>
#include <cstdint>
#include <chrono>
using U=uint32_t;
int main(){
 auto start=std::chrono::steady_clock::now();unsigned long long total=0,high=0;
 for(int gamma:{2,3})for(int same:{0,1})for(int p=0;p<=gamma;p++){
  int q=gamma-p;if((same&&q==0)||(!same&&(p==0||q==0)))continue;
  int n=3*gamma+2,z=3*gamma,w=z+1,target=(gamma*gamma+1)/2+5*gamma;
  std::vector<int>side(n);for(int d=0;d<gamma;d++){side[d]=(d<p?0:1);side[gamma+2*d]=side[gamma+2*d+1]=1-side[d];}side[z]=0;side[w]=same?0:1;
  std::vector<std::pair<int,int>>fixed,free;
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(side[u]!=side[v]){
   if(u<gamma&&v>=gamma&&v<3*gamma){if((v-gamma)/2==u)fixed.push_back({u,v});continue;}
   free.push_back({u,v});
  }
  assert(fixed.size()==size_t(2*gamma)&&free.size()<31);
  U zm=0,wm=0;for(size_t b=0;b<free.size();b++){auto [u,v]=free[b];if(u<gamma&&v==z)zm|=1u<<b;if(u<gamma&&v==w)wm|=1u<<b;}
  std::vector<U>test;U D=(1u<<gamma)-1,FULL=(1u<<n)-1;
  for(U S=1;S<=FULL;S++)if(S!=D&&__builtin_popcount(S)<=gamma)test.push_back(S);
  unsigned long long legal=0,examined=0,equality=0;
  for(U code=0;code<(1u<<free.size());code++){
   if(!(code&zm)||!(code&wm))continue;
   legal++;
   int e=fixed.size()+__builtin_popcount(code);if(e<target)continue;examined++;
   std::vector<U>closed(n);for(int i=0;i<n;i++)closed[i]=1u<<i;
   for(auto [u,v]:fixed){closed[u]|=1u<<v;closed[v]|=1u<<u;}
   for(size_t b=0;b<free.size();b++)if(code&(1u<<b)){auto [u,v]=free[b];closed[u]|=1u<<v;closed[v]|=1u<<u;}
   bool unique=true;
   for(U S:test){bool dom=true;for(U N:closed)if(!(N&S)){dom=false;break;}if(dom){unique=false;break;}}
   if(unique){if(e>target){std::cout<<"COUNTEREXAMPLE "<<gamma<<' '<<same<<' '<<p<<' '<<code<<' '<<e<<'\n';return 1;}equality++;}
  }
  total+=legal;high+=examined;
  std::cout<<"gamma="<<gamma<<" placement="<<(same?"same":"opposite")<<" p="<<p<<" q="<<q<<" legal="<<legal<<" at_or_above="<<examined<<" equality="<<equality<<'\n';
 }
 std::cout<<"PASS COMPLETE\nlegal_reduced_graphs="<<total<<"\nfull_domination_tests="<<high<<"\nseconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<'\n';
}
