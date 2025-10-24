#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; if(!(cin >> s)) return 0;

    const vector<array<string,5>> d = {
        array<string,5>{"0000","0  0","0  0","0  0","0000"},
        {"   1","   1","   1","   1","   1"},
        {"2222","   2","2222","2","2222"},
        {"3333","   3","3333","   3","3333"},
        {"4  4","4  4","4444","   4","   4"},
        {"5555","5","5555","   5","5555"},
        {"6666","6","6666","6  6","6666"},
        {"7777","   7","   7","   7","   7"},
        {"8888","8  8","8888","8  8","8888"},
        {"9999","9  9","9999","   9","   9"}
    };

    for (size_t idx = 0; idx < s.size(); ++idx) {
        int t = s[idx]-'0';
        for (int r=0;r<5;++r) cout << d[t][r] << '\n';
        if (idx+1 != s.size()) cout << '\n';
    }
}
