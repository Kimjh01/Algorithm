#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    getline(cin, s);
    int cnt = 0; 
    bool in = false;
    for (char c : s) {
        if (c != ' ') {
            if (!in){ 
                cnt++; 
             in = true; 
            }
        } else in = false;
    }
    cout << cnt << '\n';
    return 0;
}