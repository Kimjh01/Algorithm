#include <bits/stdc++.h>
using namespace std;

int main() {
    int T; 
    cin >> T;
    while (T--) {
        string s; 
        cin >> s;
        int streak = 0, total = 0;
        for (char c : s) {
            if (c == 'O') {
                streak++;
                total += streak;
            } else {
                streak = 0;
            }
        }
        cout << total << '\n';
    }
    return 0;
}
