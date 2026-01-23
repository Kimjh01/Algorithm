#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m, n;
    cin >> m >> n;
    long long digit[10] = {};
    for (long long i = m; i <= n; i++) {
        long long x = i;
        while (x > 0) {
            digit[x % 10]++;
            x /= 10;
        }
    }
    for (int i = 0; i < 10; i++) {
        cout << digit[i] << (i == 9 ? '\n' : ' ');
    }
    return 0;
}
