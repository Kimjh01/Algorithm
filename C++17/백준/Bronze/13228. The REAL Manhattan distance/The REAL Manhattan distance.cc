#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        long long x1, y1, f1, x2, y2, f2;
        cin >> x1 >> y1 >> f1 >> x2 >> y2 >> f2;
        long long dist = llabs(x1 - x2) + llabs(y1 - y2) + f1 + f2;
        cout << dist << '\n';
    }

    return 0;
}
