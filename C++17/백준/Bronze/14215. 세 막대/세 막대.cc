#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> x(3);
    for (int i = 0; i < 3; ++i) 
        cin >> x[i];
    sort(x.begin(), x.end());
    int a = x[0], b = x[1], c = x[2];
    if (a + b > c) 
        cout << (a + b + c) << '\n';
    else 
        cout << (2 * (a + b) - 1) << '\n';
    return 0;
}
