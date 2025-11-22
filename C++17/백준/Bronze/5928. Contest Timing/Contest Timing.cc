#include <bits/stdc++.h>
using namespace std;

int main() {
    int D, H, M;
    cin >> D >> H >> M;

    int t1 = D * 24 * 60 + H * 60 + M;
    int t2 = 11 * 24 * 60 + 11 * 60 + 11;
    int diff = t1 - t2;

    if (diff < 0) cout << -1 << '\n';
    else cout << diff << '\n';

    return 0;
}
