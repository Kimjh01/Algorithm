#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    cin >> M >> N;

    vector<vector<int>> ranks(M, vector<int>(N));

    for (int i = 0; i < M; i++) {
        vector<int> arr(N);
        for (int j = 0; j < N; j++) cin >> arr[j];

        vector<int> sorted = arr;
        sort(sorted.begin(), sorted.end());
        sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());

        unordered_map<int, int> mp;
        for (int r = 0; r < (int)sorted.size(); r++) {
            mp[sorted[r]] = r;
        }

        for (int j = 0; j < N; j++) {
            ranks[i][j] = mp[arr[j]];
        }
    }

    long long ans = 0;
    for (int i = 0; i < M; i++) {
        for (int j = i + 1; j < M; j++) {
            if (ranks[i] == ranks[j]) ans++;
        }
    }

    cout << ans << '\n';
    return 0;
}
