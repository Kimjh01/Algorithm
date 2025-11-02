#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long g, p, t;
    if (!(cin >> g >> p >> t)) return 0;

    long long individual = g * p;
    long long pooled = g + t * p;

    if (individual < pooled) cout << 1;
    else if (individual > pooled) cout << 2;
    else cout << 0;
    cout << "\n";
    return 0;
}
