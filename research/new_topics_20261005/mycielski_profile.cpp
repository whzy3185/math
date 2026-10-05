#include <cstdint>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main(){
 vector<uint32_t> adj={2,1};
 for(int k=2;k<=5;k++){
  int n=adj.size(); uint32_t lim=1u<<n;
  vector<uint8_t> alpha(lim,0); vector<int>w(n+1,0); vector<uint32_t>wit(n+1,0); vector<uint64_t>cnt(n+1,0);
  for(uint32_t s=1;s<lim;s++){
   unsigned v=__builtin_ctz(s);uint32_t t=s&~(1u<<v);
   alpha[s]=max(alpha[t],uint8_t(1+alpha[t&~adj[v]]));
   int a=alpha[s],c=__builtin_popcount(s);
   if(c>w[a]){w[a]=c;wit[a]=s;cnt[a]=1;}else if(c==w[a])cnt[a]++;
  }
  int ba=1,bw=0;
  cout<<"M"<<k<<" vertices="<<n<<" subsets="<<lim-1<<"\n";
  for(int a=1;a<=alpha[lim-1];a++){
   cout<<"alpha="<<a<<" max_vertices="<<w[a]<<" witness_mask="<<wit[a]<<" extremal_subsets="<<cnt[a]<<"\n";
   if(w[a]*ba>bw*a){bw=w[a];ba=a;}
  }
  cout<<"HALL_RATIO="<<bw<<"/"<<ba<<"\n";
  if(k==5)break;
  vector<uint32_t> na(2*n+1,0);
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(adj[i]&(1u<<j)){na[i]|=1u<<j;na[i]|=1u<<(j+n);na[i+n]|=1u<<j;}
  for(int i=0;i<n;i++){na[i+n]|=1u<<(2*n);na[2*n]|=1u<<(i+n);}
  adj=na;
 }
}
