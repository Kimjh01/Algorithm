#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const long long MOD = 1000000007LL;
    int t;
    cin >> t;
    vector<int> ns(t);
    int mx = 0;
    for (int i = 0; i < t; i++) {
        cin >> ns[i];
        mx = max(mx, ns[i]);
    }
    vector<long long> fact(mx + 1, 1);
    for (int i = 2; i <= mx; i++) fact[i] = (fact[i - 1] * i) % MOD;
    for (int i = 0; i < t; i++) {
        long long ans = (fact[ns[i]] - 1) % MOD;
        if (ans < 0) ans += MOD;
        cout << ans << "\n";
    }
    return 0;
}
