#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<int> cnt(4);
    for(int i = 0; i < 4; i++) cin >> cnt[i];
    string s;
    cin >> s;
    
    if(s.front() != 'a' || s.back() != 'a') {
        cout << "No";
        return 0;
    }

    for(char c : s) {
        cnt[c - 'a']--;
    }

    for(int i = 0; i < 4; i++) {
        if(cnt[i] < 0) {
            cout << "No";
            return 0;
        }
    }

    for(int i = 0; i < s.length() - 1; i++) {
        if(s[i] == s[i+1]) {
            cout << "No";
            return 0;
        }
    }

    cout << "Yes";
    return 0;
}