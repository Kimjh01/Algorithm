#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int h, m, s;
    cin >> h >> m >> s;

    int total_sec = h * 3600 + m * 60 + s;
    int q;
    cin >> q;

    while (q--) {
        int type;
        cin >> type;
        
        if (type == 3) {
            int cur_h = (total_sec / 3600) % 24;
            int cur_m = (total_sec / 60) % 60;
            int cur_s = total_sec % 60;
            cout << cur_h << " " << cur_m << " " << cur_s << "\n";
        } else {
            int t;
            cin >> t;
            if (type == 1) {
                total_sec = (total_sec + t) % 86400;
            } else if (type == 2) {
                total_sec = (total_sec - t) % 86400;
                if (total_sec < 0) total_sec += 86400; 
            }
        }
    }

    return 0;
}