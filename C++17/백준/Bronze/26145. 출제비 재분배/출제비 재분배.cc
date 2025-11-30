#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    int total = N + M;
    vector<long long> money(total, 0);

    for (int i = 0; i < N; i++) {
        cin >> money[i];
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < total; j++) {
            long long x;
            cin >> x;
            money[i] -= x;
            money[j] += x;
        }
    }

    for (int i = 0; i < total; i++) {
        cout << money[i] << " ";
    }
    return 0;
}
