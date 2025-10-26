#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n; vector<long long> ft;
    Fenwick(int n): n(n), ft(n+1,0){}
    void add(int i, long long v){ for(; i<=n; i+=i&-i) ft[i]+=v; }
    long long sum(int i){ long long s=0; for(; i>0; i-=i&-i) s+=ft[i]; return s; }
    long long range(int l,int r){ return sum(r)-sum(l-1); }
};

int main(){
    ios::sync_with_stdio(0); 
    cin.tie(0);
    int n,q; 
    if(!(cin>>n>>q)) 
        return 0;
    Fenwick fw(n);
    while(q--){
        int a,b; 
        long long c; 
        cin>>a>>b>>c;
        if(a==1) 
            fw.add(b,c);
        else     
            cout << fw.range(b,(int)c) << '\n';
    }
}
