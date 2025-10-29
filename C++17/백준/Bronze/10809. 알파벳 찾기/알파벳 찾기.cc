#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s; 
    cin >> s;
    vector<int> pos(26, -1);
    for (int i = 0; i < (int)s.size(); ++i) {
        int idx = s[i] - 'a';
        if (pos[idx] == -1) pos[idx] = i;
    }
    for (int i = 0; i < 26; ++i) {
        cout << pos[i] << (i==25?'\n':' ');
    }
    return 0;
}