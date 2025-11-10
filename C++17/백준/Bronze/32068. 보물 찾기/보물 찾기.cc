#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        long long L, R, S;
        cin >> L >> R >> S;

        long long dL = S - L;
        long long dR = R - S;

        long long ans;
        if (dL < dR) ans = dL * 2 + 1;
        else         ans = dR * 2;

        cout << ans << '\n';
    }

    return 0;
}
