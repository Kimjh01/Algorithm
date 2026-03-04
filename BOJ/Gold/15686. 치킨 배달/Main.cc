#include <bits/stdc++.h>
using namespace std;

struct Pos { int r, c; };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<Pos> houses, chickens;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int x; cin >> x;
            if (x == 1) houses.push_back({i, j});
            else if (x == 2) chickens.push_back({i, j});
        }
    }

    int H = (int)houses.size();
    int C = (int)chickens.size();

    vector<vector<int>> dist(H, vector<int>(C, 0));
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < C; ++j) {
            dist[i][j] = abs(houses[i].r - chickens[j].r) + abs(houses[i].c - chickens[j].c);
        }
    }

    const int INF = 1e9;
    int ans = INF;
    vector<int> pick;
    pick.reserve(M);

    function<void(int,int)> dfs = [&](int idx, int chosen) {
        if (chosen == M) {
            int sum = 0;
            for (int i = 0; i < H; ++i) {
                int best = INF;
                for (int cj : pick) best = min(best, dist[i][cj]);
                sum += best;
                if (sum >= ans) return;
            }
            ans = min(ans, sum);
            return;
        }
        if (idx == C) return;
        if (chosen + (C - idx) < M) return;

        pick.push_back(idx);
        dfs(idx + 1, chosen + 1);
        pick.pop_back();

        dfs(idx + 1, chosen);
    };

    dfs(0, 0);
    cout << ans << "\n";
    return 0;
}