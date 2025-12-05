#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    int matchO = min(M, K);
    int matchX = min(N - M, N - K);

    cout << matchO + matchX << endl;

    return 0;
}