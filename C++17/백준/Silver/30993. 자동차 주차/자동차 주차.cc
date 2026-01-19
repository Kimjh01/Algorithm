#include <iostream>

using namespace std;

int main() {
    int N, A, B, C;
    cin >> N >> A >> B >> C;

    long long fact[16];
    fact[0] = 1;
    for (int i = 1; i <= 15; ++i) fact[i] = fact[i - 1] * i;

    long long ans = fact[N] / (fact[A] * fact[B] * fact[C]);
    cout << ans;

    return 0;
}