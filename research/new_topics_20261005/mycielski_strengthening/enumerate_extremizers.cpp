// Exact structurally reduced enumeration. No optimizer or floating point.
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <chrono>
#include <functional>
#include <cassert>
using namespace std;
using U=uint32_t; using W=uint64_t;
struct IS {U I,N;int s;};
int main(){
 auto start=chrono::steady_clock::now();
 vector<U> adj={2,1};
 for(int r=2;r<5;r++){int n=adj.size();vector<U>b(2*n+1);for(int i=0;i<n;i++){b[i]=adj[i]|(adj[i]<<n);b[n+i]=adj[i]|(1u<<(2*n));b[2*n]|=1u<<(n+i);}adj=b;}
 U full=(1u<<23)-1;
 vector<vector<int>>group;
 int cyc[5]={0,1,2,4,3};
 for(int sign:{1,-1})for(int shift=0;shift<5;shift++){
  vector<int>p(5);for(int i=0;i<5;i++)p[cyc[i]]=cyc[(sign*i+shift+10)%5];
  for(int level=0;level<2;level++){int n=p.size();vector<int>q=p;for(int v:p)q.push_back(n+v);q.push_back(2*n);p=q;}group.push_back(p);
 }
 auto image=[&](U A,const vector<int>&p){U B=0;while(A){int v=__builtin_ctz(A);A&=A-1;B|=1u<<p[v];}return B;};
 auto canonicalA=[&](U A){U best=A;for(auto&p:group)best=min(best,image(A,p));return best;};
 auto canonicalW=[&](U A,U B){W best=~W(0);for(auto&p:group)best=min(best,W(image(A,p))|(W(image(B,p))<<23)|(W(1)<<46));return best;};
 vector<IS> indep;
 function<void(U,U,U)>visit=[&](U P,U I,U N){indep.push_back({I,N,__builtin_popcount(I)});while(P){int v=__builtin_ctz(P);P&=P-1;visit(P&~adj[v],I|(1u<<v),N|adj[v]);}};
 visit(full,0,0);assert(indep.size()==7407);
 vector<uint8_t>alpha(1u<<23);vector<U>As;
 for(U A=1;A<=full;A++){int v=__builtin_ctz(A);U T=A&(A-1);alpha[A]=max(alpha[T],uint8_t(1+alpha[T&~adj[v]]));int a=__builtin_popcount(A);if(alpha[A]<=5)assert(a<=15);if(alpha[A]<=4)assert(a<=12);if(a>=13&&a<=15&&alpha[A]<=5&&canonicalA(A)==A){assert(alpha[A]==5);As.push_back(A);}}
 cerr<<"canonical original sets "<<As.size()<<'\n';
 map<pair<U,int>,vector<U>>bcache;
 auto Bs=[&](U N,int b)->const vector<U>&{
  auto key=make_pair(N,b);auto found=bcache.find(key);if(found!=bcache.end())return found->second;
  vector<U>v;U C=full^N;
  function<void(U,int,U,int)>choose=[&](U pool,int k,U X,int inside){
   if(k==0){if(inside==0)v.push_back(X);else{U q=C;while(q){U bit=q&-q;q^=bit;v.push_back(X|bit);}}return;}
   while(__builtin_popcount(pool)>=k){U bit=pool&-pool;pool^=bit;choose(pool,k-1,X|bit,inside);}
  };
  choose(N,b,0,0);choose(N,b-1,0,1);
  return bcache.emplace(key,move(v)).first->second;
 };
 set<W>orbits;unsigned long long tested=0,accepted=0;size_t processed=0;
 for(U A:As){
  if(chrono::duration<double>(chrono::steady_clock::now()-start).count()>90){cerr<<"INCOMPLETE TIME LIMIT\n";return 2;}
  vector<pair<U,int>>constraints;U bestN=full;
  int b=19-__builtin_popcount(A);
  for(auto t:indep)if((t.I&~A)==0&&t.s>6-b){constraints.push_back({full^t.N,6-t.s});if(t.s==5&&__builtin_popcount(t.N)<__builtin_popcount(bestN))bestN=t.N;}
  sort(constraints.begin(),constraints.end(),[](auto a,auto b){if(a.second!=b.second)return a.second<b.second;return __builtin_popcount(a.first)>__builtin_popcount(b.first);});
  constraints.erase(unique(constraints.begin(),constraints.end()),constraints.end());
  for(U B:Bs(bestN,b)){
   tested++;bool okay=true;
   for(auto [C,cap]:constraints)if(__builtin_popcount(B&C)>cap){okay=false;break;}
   if(okay){accepted++;orbits.insert(canonicalW(A,B));}
  }
  processed++;
 }
 ofstream out("complete_orbit_representatives.txt");for(W S:orbits)out<<S<<'\n';
 cout<<"COMPLETE\ncanonical_original_sets="<<processed<<"\nclone_candidates_tested="<<tested<<"\naccepted_at_canonical_A="<<accepted<<"\norbits="<<orbits.size()<<"\nseconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<'\n';
}
