#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    int m = n * n;
    vector<int> cnt(m + 1, 0);

    for (int d = 1; d <= m; d++) {
        for (int x = d; x <= m; x += d) cnt[x]++;
    }

    for (int i = 1; i <= m; i++) {
        cout << (cnt[i] <= k ? '*' : '.');
        if (i % n == 0) cout << "\n";
    }
    return 0;
}
