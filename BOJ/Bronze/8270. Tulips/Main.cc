#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    unordered_set<int> s;
    s.reserve(N * 2 + 1);
    for (int i = 0; i < N; i++) {
        int x;
        cin >> x;
        s.insert(x);
    }
    cout << (15000 - (int)s.size()) << "\n";
    return 0;
}
