#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; string s;
    cin >> n >> s;

    int S = count(s.begin(), s.end(), 's');
    int T = count(s.begin(), s.end(), 't');

    int i = 0;
    while (i < n && S != T) {
        if (s[i] == 's') --S;
        else             --T;   
        ++i;
    }
    cout << s.substr(i) << '\n';
    return 0;
}
