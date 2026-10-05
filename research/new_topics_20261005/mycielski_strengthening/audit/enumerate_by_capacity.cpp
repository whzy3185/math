// Independent complete M6 apex-extremizer enumeration.
// Alpha: max subset-zeta transform. Clones: recursive capacity propagation.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using Mask=uint32_t; using Big=uint64_t;
int pc(Mask x){return __builtin_popcount(x);}
std::vector<Mask> mu(const std::vector<Mask>&a){
 int n=a.size();std::vector<Mask>b(2*n+1);
 for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(a[u]&(Mask(1)<<v)){
  b[u]|=Mask(1)<<v;b[v]|=Mask(1)<<u;
  b[u]|=Mask(1)<<(n+v);b[n+v]|=Mask(1)<<u;
  b[v]|=Mask(1)<<(n+u);b[n+u]|=Mask(1)<<v;
 }
 for(int u=0;u<n;u++){b[n+u]|=Mask(1)<<(2*n);b[2*n]|=Mask(1)<<(n+u);}
 return b;
}
Mask image(Mask a,const std::vector<int>&p){Mask b=0;while(a){int i=__builtin_ctz(a);a&=a-1;b|=Mask(1)<<p[i];}return b;}
struct Constraint{Mask mask;int cap;};
int main(){
 auto start=std::chrono::steady_clock::now();
 auto c5=mu({2,1});auto g=mu(mu(c5));assert(g.size()==23);
 std::vector<std::vector<int>>group;std::vector<int>p(5);std::iota(p.begin(),p.end(),0);
 do{
  bool ok=true;for(int u=0;u<5;u++)for(int v=0;v<5;v++)if(bool(c5[u]&(1<<v))!=bool(c5[p[u]]&(1<<p[v])))ok=false;
  if(ok){auto q=p;for(int level=0;level<2;level++){int n=q.size();auto qq=q;for(int v:q)qq.push_back(n+v);qq.push_back(2*n);q=qq;}group.push_back(q);}
 }while(std::next_permutation(p.begin(),p.end()));
 assert(group.size()==10);const Mask FULL=(Mask(1)<<23)-1;
 std::vector<Mask>ind;
 std::function<void(Mask,Mask)>sets=[&](Mask pool,Mask chosen){
  if(!pool){ind.push_back(chosen);return;}
  Mask bit=pool&-pool;int v=__builtin_ctz(bit);pool^=bit;
  sets(pool,chosen);sets(pool&~g[v],chosen|bit);
 };sets(FULL,0);assert(ind.size()==7407);
 std::vector<Mask>neighborhoods;for(Mask I:ind){Mask n=0;for(int v=0;v<23;v++)if(I&(1<<v))n|=g[v];neighborhoods.push_back(n);}
 std::vector<uint8_t>alpha(Mask(1)<<23,0);for(Mask I:ind)alpha[I]=pc(I);
 for(int v=0;v<23;v++){Mask bit=Mask(1)<<v;for(Mask base=0;base<=FULL;base+=bit*2)for(Mask low=0;low<bit;low++)alpha[base+bit+low]=std::max(alpha[base+bit+low],alpha[base+low]);}
 int max4=0,max5=0;std::array<int,24>labelledA{},canonicalA{};std::vector<Mask>originals;
 for(Mask A=0;A<=FULL;A++){
  int sz=pc(A);if(alpha[A]<=4)max4=std::max(max4,sz);if(alpha[A]<=5)max5=std::max(max5,sz);
  if(sz<13||sz>15||alpha[A]>5)continue;
  labelledA[sz]++;bool canonical=true;for(auto&q:group)if(image(A,q)<A){canonical=false;break;}
  if(canonical){originals.push_back(A);canonicalA[sz]++;}
 }
 assert(max4==12&&max5==15);assert(originals.size()==4370);
 std::set<Big>orbits;uint64_t nodes=0,accepted=0;std::array<int,24>acceptedLayer{};
 for(Mask A:originals){
  const int b=19-pc(A);std::vector<Constraint>all,cons;
  for(size_t i=0;i<ind.size();i++)if(!(ind[i]&~A)){
   int cap=6-pc(ind[i]);if(cap<b)all.push_back({FULL^neighborhoods[i],cap});
  }
  std::sort(all.begin(),all.end(),[](auto x,auto y){if(x.cap!=y.cap)return x.cap<y.cap;return pc(x.mask)>pc(y.mask);});
  for(auto c:all){bool dominated=false;for(auto d:cons)if(c.cap>=d.cap&&!(c.mask&~d.mask)){dominated=true;break;}if(!dominated)cons.push_back(c);}
  std::array<int,23>score{};for(auto c:cons)for(int v=0;v<23;v++)if(c.mask&(1<<v))score[v]+=12/(c.cap+1);
  std::function<void(Mask,Mask,int)>search=[&](Mask pool,Mask B,int need){
   nodes++;Mask banned=0;
   for(auto c:cons){int slack=c.cap-pc(B&c.mask);if(slack<0)return;if(slack==0)banned|=c.mask;}
   pool&=~banned;if(pc(pool)<need)return;
   for(auto c:cons)if(need>pc(pool&~c.mask)+c.cap-pc(B&c.mask))return;
   if(need==0){
    assert(pc(B)==b);for(auto c:all)assert(pc(B&c.mask)<=c.cap);
    Big best=~Big(0);for(auto&q:group)best=std::min(best,Big(image(A,q))|(Big(image(B,q))<<23)|(Big(1)<<46));
    orbits.insert(best);accepted++;acceptedLayer[pc(A)]++;return;
   }
   int v=-1;for(int w=0;w<23;w++)if(pool&(1<<w))if(v<0||score[w]>score[v])v=w;
   assert(v>=0);Mask bit=Mask(1)<<v;pool^=bit;
   search(pool,B,need);search(pool,B|bit,need-1);
  };search(FULL,0,b);
 }
 std::ofstream f("independent_representatives.txt");for(Big x:orbits)f<<x<<'\n';
 std::cout<<"COMPLETE\nindependent_sets="<<ind.size()<<"\nalpha_max_size_at_4="<<max4<<"\nalpha_max_size_at_5="<<max5<<'\n';
 for(int a=13;a<=15;a++)std::cout<<"originals_size_"<<a<<'='<<labelledA[a]<<" canonical="<<canonicalA[a]<<" accepted="<<acceptedLayer[a]<<'\n';
 std::cout<<"canonical_originals="<<originals.size()<<"\nsearch_nodes="<<nodes<<"\naccepted="<<accepted<<"\norbits="<<orbits.size()<<"\nseconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<'\n';
}
