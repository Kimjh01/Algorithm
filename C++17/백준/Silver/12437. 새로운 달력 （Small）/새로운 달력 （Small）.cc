#include <iostream>
using namespace std;
int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        long long m, d, w;
        cin >> m >> d >> w;
        long long total = 0, cur = 0;
        for (int j = 0; j < m; j++) {
            total += (cur + d + w - 1) / w;
            cur = (cur + d) % w;
        }
        cout << "Case #" << i << ": " << total << endl;
    }
    return 0;
}