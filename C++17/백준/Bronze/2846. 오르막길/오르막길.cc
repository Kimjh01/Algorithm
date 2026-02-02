#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    int best = 0;
    int start = a[0];
    for (int i = 1; i < N; i++) {
        if (a[i] > a[i - 1]) {
            best = max(best, a[i] - start);
        } else {
            start = a[i];
        }
    }
    cout << best << "\n";
    return 0;
}
