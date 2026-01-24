#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    bool broken[256] = {};
    int k;
    cin >> k;
    for (int i = 0; i < k; i++) {
        char x;
        cin >> x;
        broken[(unsigned char)x] = true;
    }
    int target;
    cin >> target;

    int ans = 1000000000;
    for (int i = 0; i < 1000; i++) {
        string s = to_string(i);
        bool bad = false;
        for (char c : s) if (broken[(unsigned char)c]) { bad = true; break; }
        if (bad) continue;
        ans = min(ans, abs(target - i));
    }
    cout << ans;
    return 0;
}
