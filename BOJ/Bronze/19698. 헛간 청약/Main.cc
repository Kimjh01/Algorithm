#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long N, W, H, L;
    cin >> N >> W >> H >> L;
    long long a = W / L;
    long long b = H / L;
    long long can = a * b;
    cout << min(N, can);
    return 0;
}
