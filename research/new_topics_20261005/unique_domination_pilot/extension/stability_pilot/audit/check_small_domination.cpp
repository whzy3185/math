// Independently reconstructed family; exhaustive domination through size 2k.
#include <vector>
#include <iostream>
#include <cstdint>
#include <functional>
#include <cassert>
using U=uint64_t;
int main(){
 for(int k=2;k<=4;k++)for(int s=1;s<k;s++){
  int n=6*k+1,g=2*k,z=6*k;std::vector<U>N(n);for(int v=0;v<n;v++)N[v]=U(1)<<v;
  auto edge=[&](int u,int v){assert(!(N[u]&(U(1)<<v)));N[u]|=U(1)<<v;N[v]|=U(1)<<u;};
  for(int i=0;i<k;i++){
   int x=i,u0=2*k+2*i,u1=u0+1;edge(x,u0);edge(x,u1);edge(z,u1);
   if(i>=s)edge(z,u0);
   for(int j=0;j<k;j++){
    int y=k+j,v0=4*k+2*j;
    edge(u1,v0);
    if(i<s)edge(x,y);else edge(u0,v0);
   }
  }
  for(int j=0;j<k;j++){int y=k+j;edge(y,4*k+2*j);edge(y,4*k+2*j+1);edge(z,y);}
  U D=(U(1)<<g)-1;unsigned long long tested=0,dominating=0;U last=0;
  std::function<void(int,int,U)>choose=[&](int next,int left,U S){
   if(!left){tested++;bool good=true;for(U C:N)if(!(C&S)){good=false;break;}if(good){dominating++;last=S;assert(S==D);}return;}
   for(int v=next;v<=n-left;v++)choose(v+1,left-1,S|(U(1)<<v));
  };
  for(int a=0;a<=g;a++)choose(0,a,0);
  assert(dominating==1&&last==D);int edges=0;for(U C:N)edges+=__builtin_popcountll(C)-1;edges/=2;
  assert(edges==2*k*k+7*k-s);
  std::cout<<"k="<<k<<" s="<<s<<" n="<<n<<" gamma="<<g<<" edges="<<edges<<" checked="<<tested<<" unique_minimum=true\n";
 }
 std::cout<<"PASS\n";
}
