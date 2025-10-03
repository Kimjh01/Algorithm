#include <bits/stdc++.h>
using namespace std;

static inline bool isV(char c){
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s; 
    getline(cin, s);
    string out;
    for (size_t i = 0; i < s.size(); ) {
        out.push_back(s[i]);
        if (isV(s[i]) && i + 2 < s.size()) 
            i += 3;
        else ++i;
    }
    cout << out << '\n';
    return 0;
}

