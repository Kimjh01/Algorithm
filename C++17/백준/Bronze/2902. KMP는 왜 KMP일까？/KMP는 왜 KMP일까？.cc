#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s; 
    if (!(cin >> s)) 
        return 0;
    cout << s[0];
    for (size_t i = 0; i + 1 < s.size(); ++i)
        if (s[i] == '-') 
            cout << s[i + 1];
    cout << '\n';
    return 0;
}
