#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;

    vector<int> first(26, -1), second(26, -1);
    for (int i = 0; i < (int)s.size(); i++) {
        int idx = s[i] - 'A';
        if (first[idx] == -1) first[idx] = i;
        else second[idx] = i;
    }

    int ans = 0;
    for (int i = 0; i < 26; i++) {
        for (int j = i + 1; j < 26; j++) {
            int a1 = first[i], a2 = second[i];
            int b1 = first[j], b2 = second[j];
            if (a1 > a2) swap(a1, a2);
            if (b1 > b2) swap(b1, b2);
            if (a1 < b1 && b1 < a2 && a2 < b2) ans++;
            else if (b1 < a1 && a1 < b2 && b2 < a2) ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
