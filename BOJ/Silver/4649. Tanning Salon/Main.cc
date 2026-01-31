#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (true) {
        int n;
        if (!(cin >> n)) 
            return 0;
        if (n == 0) 
            break;

        string s;
        cin >> s;

        unordered_set<char> inside, rejected;
        inside.reserve(128);
        rejected.reserve(128);

        int walked = 0;
        for (char c : s) {
            if (inside.find(c) != inside.end()) {
                inside.erase(c);
            } else if (rejected.find(c) != rejected.end()) {
                rejected.erase(c);
            } else {
                if ((int)inside.size() < n) inside.insert(c);
                else {
                    rejected.insert(c);
                    walked++;
                }
            }
        }

        if (walked == 0) cout << "All customers tanned successfully.\n";
        else cout << walked << " customer(s) walked away.\n";
    }
    return 0;
}
