#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    while (cin >> n && n != 0) {
        vector<pair<int, int>> p(n);
        for (int i = 0; i < n; i++) cin >> p[i].first >> p[i].second;
        int cx = p[n / 2].first, cy = p[n / 2].second;
        int stan = 0, ollie = 0;
        for (int i = 0; i < n; i++) {
            int dx = p[i].first - cx, dy = p[i].second - cy;
            if (dx == 0 || dy == 0) continue;
            if ((dx > 0 && dy > 0) || (dx < 0 && dy < 0)) stan++;
            else ollie++;
        }
        cout << stan << " " << ollie << endl;
    }
    return 0;
}