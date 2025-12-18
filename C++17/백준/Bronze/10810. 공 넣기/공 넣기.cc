#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> basket(N + 1, 0);

    for (int q = 0; q < M; ++q) {
        int i, j, k;
        cin >> i >> j >> k;
        for (int idx = i; idx <= j; ++idx) {
            basket[idx] = k;
        }
    }

    for (int i = 1; i <= N; ++i) {
        cout << basket[i] << (i == N ? "" : " ");
    }

    return 0;
}