#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s1, s2;        
    if (!(cin >> s1 >> s2)) return 0;

    auto to_sec = [](const string& t) {
        int h = stoi(t.substr(0, 2));
        int m = stoi(t.substr(3, 2));
        int s = stoi(t.substr(6, 2));
        return h * 3600 + m * 60 + s;
    };

    int t1 = to_sec(s1);
    int t2 = to_sec(s2);

    const int DAY = 24 * 3600;
    int diff = (t2 - t1) % DAY;
    if (diff < 0) diff += DAY;

    if (diff == 0) {
        cout << "24:00:00\n";
    } else {
        int h = diff / 3600;
        int m = (diff % 3600) / 60;
        int s = diff % 60;
        cout << setw(2) << setfill('0') << h << ":"
             << setw(2) << setfill('0') << m << ":"
             << setw(2) << setfill('0') << s << "\n";
    }
    return 0;
}