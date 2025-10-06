#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N; 
    if (!(cin >> N)) return 0;
    for (int i = 1; i <= N; ++i) {
        cout << string(N - i, ' ') << string(i, '*') << '\n';
    }
    return 0;
}
