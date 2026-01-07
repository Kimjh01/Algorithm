#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n, k_cnt;
    cin >> n >> k_cnt;
    vector<int> k(k_cnt);
    for (int i = 0; i < k_cnt; i++) cin >> k[i];
    vector<long long> v = {0};
    long long ans = 0;
    int head = 0;
    while(head < v.size()){
        long long curr = v[head++];
        for(int i=0; i<k_cnt; i++){
            long long nxt = curr * 10 + k[i];
            if(nxt <= n){
                if(nxt > ans) ans = nxt;
                v.push_back(nxt);
            }
        }
    }
    cout << ans << endl;
    return 0;
}