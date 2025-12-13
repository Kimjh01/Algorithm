#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int m, h, n;
    cin >> m >> h >> n;
    long long ans = 0;
    while(n--) {
        int c, b;
        cin >> c >> b;
        ans += max(c * m, b * h);
    }
    cout << ans << "\n";
    return 0;
}