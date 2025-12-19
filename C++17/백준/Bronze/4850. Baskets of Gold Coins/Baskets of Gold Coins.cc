#include <iostream>

using namespace std;

int main() {
    long long N, w, d, S;
    while (cin >> N >> w >> d >> S) {
        long long totalCoins = N * (N - 1) / 2;
        long long expectedWeight = totalCoins * w;
        long long diff = expectedWeight - S;

        if (diff == 0) {
            cout << N << endl;
        } else {
            cout << diff / d << endl;
        }
    }
    return 0;
}