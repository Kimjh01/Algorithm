#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    double p[10];
    for (int i = 0; i < 10; i++) cin >> p[i];
    sort(p, p + 10);
    double ans = 1.0;
    for (int i = 1; i < 10; i++) ans *= p[i];
    cout << fixed << setprecision(6) << ans / 362880.0 * 1e9;
    return 0;
}