#include <bits/stdc++.h>
using namespace std;

int fact(int n) {
    int res = 1;
    for (int i = 2; i <= n; i++) res *= i;
    return res;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    while (true) {
        cin >> s;
        if (s == "0") 
            break;

        int len = s.length();
        int ans = 0;

        for (int i = 0; i < len; i++) {
            int digit = s[len - 1 - i] - '0'; 
            ans += digit * fact(i + 1);
        }

        cout << ans << "\n";
    }
    return 0;
}
