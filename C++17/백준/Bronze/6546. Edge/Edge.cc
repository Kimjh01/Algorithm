#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string t;
    while (getline(cin, t)) {
        int x = 300, y = 420;
        int dir = 0;
        cout << x << " " << y << " moveto\n";
        x += 10;
        cout << x << " " << y << " lineto\n";

        for (char c : t) {
            if (c == 'A') dir = (dir + 3) % 4;
            else dir = (dir + 1) % 4;

            if (dir == 0) x += 10;
            else if (dir == 1) y += 10;
            else if (dir == 2) x -= 10;
            else y -= 10;

            cout << x << " " << y << " lineto\n";
        }
        cout << "stroke\n";
        cout << "showpage\n";
    }
    return 0;
}
