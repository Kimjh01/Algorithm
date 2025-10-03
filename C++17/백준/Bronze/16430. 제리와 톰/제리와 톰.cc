#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int A, B;
    if (!(cin >> A >> B)) return 0;
    cout << (B - A) << ' ' << B << '\n';
    return 0;
}