#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    vector<int> max_prime(N + 1, 0);

    for (int i = 2; i <= N; ++i) {
        if (max_prime[i] == 0) { 
            for (int j = i; j <= N; j += i) {
                max_prime[j] = i;
            }
        }
    }

    int count = 0;
    for (int i = 1; i <= N; ++i) {
        if (max_prime[i] <= K) {
            count++;
        }
    }

    cout << count;

    return 0;
}