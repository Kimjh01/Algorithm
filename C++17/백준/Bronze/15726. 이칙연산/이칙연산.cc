#include <bits/stdc++.h>
using namespace std;

int main() {
    double a, b, c;
    cin >> a >> b >> c;

    double x = (a * b) / c;
    double y = (a / b) * c;

    double mx = max(x, y);
    long long ans = (long long)mx;  

    cout << ans << '\n';
    return 0;
}
