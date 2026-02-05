#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int gcd(int a, int b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n; cin >> n;
    vector<int> v(n), diff;
    for (int i = 0; i < n; i++) cin >> v[i];
    int g = 0;
    for (int i = 0; i < n - 1; i++) {
        int d = v[i+1] - v[i];
        g = (i == 0) ? d : gcd(g, d);
    }
    long long ans = 0;
    for (int i = 0; i < n - 1; i++) ans += (v[i+1] - v[i]) / g - 1;
    cout << ans;
    return 0;
}