#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int q;
    cin >> q;
    while(q--) {
        string s;
        cin >> s;
        int ans = 0;
        int len = s.length();
        for(int i = 0; i + 2 < len; i++) {
            if(s[i] == 'W' && s[i+1] == 'O' && s[i+2] == 'W') {
                ans++;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}