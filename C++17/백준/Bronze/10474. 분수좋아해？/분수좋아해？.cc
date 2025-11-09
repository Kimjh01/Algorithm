#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    while (true) {
        cin >> a >> b;
        if (a == 0 && b == 0) break;

        long long q = a / b; 
        long long r = a % b;  

        cout << q << ' ' << r << " / " << b << '\n';
    }

    return 0;
}