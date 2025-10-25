#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    long long k, n; if(!(cin >> k >> n)) return 0;
    cout << (n + 1) << ' ' << (k * n + 1);
}
