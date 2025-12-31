#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long a, prev = LLONG_MIN;
    cin >> N;
    while (N--) {
        cin >> a;
        if (a <= prev) {
            cout << 0;
            return 0;
        }
        prev = a;
    }
    cout << 1;
    return 0;
}
