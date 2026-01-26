#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    int c2 = 0, c0 = 0, c1 = 0, c8 = 0;
    for (char ch : s) {
        if (ch == '2') c2++;
        else if (ch == '0') c0++;
        else if (ch == '1') c1++;
        else if (ch == '8') c8++;
        else {
            cout << 0;
            return 0;
        }
    }
    bool has2 = c2 > 0, has0 = c0 > 0, has1 = c1 > 0, has8 = c8 > 0;
    if (has2 && has0 && has1 && has8) {
        if (c2 == c0 && c0 == c1 && c1 == c8) cout << 8;
        else cout << 2;
    } else {
        cout << 1;
    }
    return 0;
}
