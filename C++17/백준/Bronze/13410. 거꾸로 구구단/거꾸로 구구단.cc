#include <bits/stdc++.h>
using namespace std;

int reverseNum(int x) {
    int r = 0;
    while (x > 0) {
        r = r * 10 + (x % 10);
        x /= 10;
    }
    return r;
}

int main() {
    int N, K;
    cin >> N >> K;

    int ans = 0;
    for (int i = 1; i <= K; i++) {
        int val = N * i;
        int rev = reverseNum(val);
        ans = max(ans, rev);
    }
    cout << ans << '\n';
    return 0;
}
