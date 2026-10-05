// Independent exact tests of slack, good-block coherence and labelled repair.
#include <vector>
#include <iostream>
#include <functional>
#include <cassert>
#include <cstdint>
using U=uint32_t;
unsigned long long candidates=0,unique_cases=0,multi=0,single=0,zero=0;
int pop(U x){return __builtin_popcount(x);}
void edge(std::vector<U>&A,int u,int v){assert(!(A[u]&(1u<<v)));A[u]|=1u<<v;A[v]|=1u<<u;}
bool dom(U S,const std::vector<U>&A){for(int v=0;v<(int)A.size();v++)if(!(((1u<<v)|A[v])&S))return false;return true;}
bool uniqueD(const std::vector<U>&A,int g){
 U D=(1u<<g)-1;assert(dom(D,A));int n=A.size();
 std::function<bool(int,int,U)>visit=[&](int next,int left,U S){
  if(!left)return S==D||!dom(S,A);
  for(int v=next;v<=n-left;v++)if(!visit(v+1,left-1,S|(1u<<v)))return false;
  return true;
 };
 for(int k=0;k<=g;k++)if(!visit(0,k,0))return false;
 return true;
}
std::vector<U> fixed(int g){std::vector<U>A(3*g+1);for(int d=0;d<g;d++){edge(A,d,g+2*d);edge(A,d,g+2*d+1);}return A;}
void audit(const std::vector<U>&A,int p,int q){
 candidates++;int g=p+q,n=A.size(),z=3*g;assert(n==3*g+1);if(!uniqueD(A,g))return;unique_cases++;
 int e=0;for(U row:A)e+=pop(row);assert(e%2==0);e/=2;int M=g*(g+7)/2,t=M-e;assert(t>=0);
 int d=p-q,B=d*(d-1)/2;U D=(1u<<g)-1;int owners=pop(A[z]&D);assert(owners>0);
 if(t==0)zero++;
 if(owners==1){single++;assert(t>=B+q-1);assert(t>=(g-2)/2);if(t)assert(e+M<=12*g*t);return;}
 multi++;
 int R=2*p+q-pop(A[z]),L=0,bX=0,bY=0;
 std::vector<bool>goodRow(p),goodCol(q);std::vector<int>selected(q,-1);std::vector<std::vector<int>>K(p,std::vector<int>(q));
 for(int i=0;i<p;i++){int u=g+2*i;goodRow[i]=(A[z]&(1u<<u))&&(A[z]&(1u<<(u+1)));if(!goodRow[i])bX++;}
 for(int j=0;j<q;j++){goodCol[j]=A[z]&(1u<<(p+j));if(!goodCol[j])bY++;}
 for(int i=0;i<p;i++)for(int j=0;j<q;j++){
  int u=g+2*i,v=g+2*(p+j);int cell=bool(A[i]&(1u<<(p+j)));
  for(int a=0;a<2;a++)for(int b=0;b<2;b++)cell+=bool(A[u+a]&(1u<<(v+b)));
  assert(cell<=2);K[i][j]=cell;L+=2-cell;
  if(goodRow[i])assert(!(A[i]&(1u<<(p+j))));
  if(goodRow[i]&&goodCol[j]&&cell==2){
   int choice=-1;for(int b=0;b<2;b++)if((A[u]&(1u<<(v+b)))&&(A[u+1]&(1u<<(v+b))))choice=b;
   assert(choice>=0);if(selected[j]>=0)assert(selected[j]==choice);selected[j]=choice;
  }
 }
 assert(B>=0&&L>=0&&R>=0&&t==B+L+R);
 auto T=fixed(g);
 for(int i=0;i<p;i++)for(int j=0;j<q;j++)for(int b=0;b<2;b++)edge(T,g+2*i+b,g+2*(p+j)+(selected[j]<0?0:selected[j]));
 for(int i=0;i<p;i++){edge(T,z,g+2*i);edge(T,z,g+2*i+1);}for(int j=0;j<q;j++)edge(T,z,p+j);
 int diff=0;for(int i=0;i<n;i++)diff+=pop(A[i]^T[i]);assert(diff%2==0);diff/=2;
 assert(diff<=R+4*L+4*(q*bX+p*bY));assert(diff<=(4*g+1)*t);
}
int main(){
 // Every selected-private-pair skeleton at gamma2 and gamma3.
 for(int g:{2,3})for(int p=0;p<g;p++){
  int q=g-p,n=3*g+1,z=3*g;auto F=fixed(g);std::vector<int>side(n);for(int d=0;d<g;d++){side[d]=d<p?0:1;side[g+2*d]=side[g+2*d+1]=1-side[d];}side[z]=0;
  std::vector<std::pair<int,int>>free;U owner=0;
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(side[u]!=side[v]&&!(F[u]&(1u<<v))){if(u<g&&v<3*g&&v>=g)continue;int bit=free.size();free.push_back({u,v});if(u<g&&v==z)owner|=1u<<bit;}
  for(U code=0;code<(1u<<free.size());code++)if(code&owner){auto A=F;for(size_t b=0;b<free.size();b++)if(code&(1u<<b))edge(A,free[b].first,free[b].second);audit(A,p,q);}
 }
 // Generate all valid six-cell patterns independently (14 patterns).
 std::vector<U>pal;for(U code=0;code<32;code++){
  std::vector<U>A(6);edge(A,0,2);edge(A,0,3);edge(A,1,4);edge(A,1,5);std::vector<std::pair<int,int>>free={{0,1},{2,4},{2,5},{3,4},{3,5}};
  for(int b=0;b<5;b++)if(code&(1u<<b))edge(A,free[b].first,free[b].second);
  if(uniqueD(A,2))pal.push_back(code);
 }assert(pal.size()==14);
 // gamma4,p=q=2 with both residual owners and arbitrary residual U incidences.
 for(U a:pal)for(U b:pal)for(U c:pal)for(U d:pal)for(U tail=0;tail<16;tail++){
  int g=4,z=12;auto A=fixed(g);edge(A,z,2);edge(A,z,3);for(int v=0;v<4;v++)if(tail&(1u<<v))edge(A,z,4+v);U cells[4]={a,b,c,d};
  for(int i=0;i<2;i++)for(int j=0;j<2;j++){
   int u=4+2*i,v=8+2*j;std::vector<std::pair<int,int>>free={{i,2+j},{u,v},{u,v+1},{u+1,v},{u+1,v+1}};
   for(int bit=0;bit<5;bit++)if(cells[2*i+j]&(1u<<bit))edge(A,free[bit].first,free[bit].second);
  }audit(A,2,2);
 }
 std::cout<<"PASS\ncandidate_graphs="<<candidates<<"\nunique_minimum_graphs="<<unique_cases<<"\nmultiple_owner="<<multi<<"\nsingle_owner="<<single<<"\nzero_deficit="<<zero<<"\n";
}
