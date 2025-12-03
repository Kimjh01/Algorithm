#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int A, B, X;
        cin >> A >> B >> X;
        cout << A * (X - 1) + B << "\n";
    }

    return 0;
}