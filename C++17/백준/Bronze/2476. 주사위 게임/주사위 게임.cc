#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    int max_reward = 0;

    for (int i = 0; i < N; ++i) {
        int a, b, c;
        cin >> a >> b >> c;

        int reward = 0;
        if (a == b && b == c) {
            reward = 10000 + a * 1000;
        } else if (a == b || a == c) {
            reward = 1000 + a * 100;
        } else if (b == c) {
            reward = 1000 + b * 100;
        } else {
            reward = max({a, b, c}) * 100;
        }

        if (reward > max_reward) {
            max_reward = reward;
        }
    }

    cout << max_reward;
    return 0;
}