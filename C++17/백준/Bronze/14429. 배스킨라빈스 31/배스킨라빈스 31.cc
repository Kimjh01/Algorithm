#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    long long bestTurns = LLONG_MAX;
    int bestIdx = 0;

    for (int i = 1; i <= n; i++) {
        long long j, m;
        cin >> j >> m;

        long long r = (j - 1) % (m + 1);
        long long k = (j - r) / (m + 1);   
        long long turns = (k + 1) * 2;    

        if (turns < bestTurns) {
            bestTurns = turns;
            bestIdx = i;
        }
    }

    cout << bestIdx << ' ' << bestTurns << '\n';
    return 0;
}
