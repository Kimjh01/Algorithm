#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cout.setf(std::ios::fixed);
    cout.precision(10);

    int T;
    cin >> T;
    while (T--) {
        int h, m, s;
        cin >> h >> m >> s;
        int a[3];
        a[0] = 3600 * h + 60 * m + s;
        a[1] = 720 * m + 12 * s;
        a[2] = 720 * s;
        sort(a, a + 3);
        int mx = min(min(a[1] - a[0], a[2] - a[1]), 43200 + a[0] - a[2]);
        cout << (double)mx / 120.0 << "\n";
    }
    return 0;
}
