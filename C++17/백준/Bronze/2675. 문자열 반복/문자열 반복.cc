#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T; 
    cin >> T;
    while (T--) {
        int R; 
        string s; 
        cin >> R >> s;
        for (char c : s) 
            for (int i = 0; i < R; ++i) 
                cout << c;
        cout << '\n';
    }
    return 0;
}