#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    while (cin >> n && n) {
        long long a = n, b = n + 1, c = n + 2;

        if (a % 2 == 0) a /= 2;
        else b /= 2;

        if (a % 3 == 0) a /= 3;
        else if (b % 3 == 0) b /= 3;
        else c /= 3;

        cout << a * b * c << '\n';
    }
    return 0;
}
