#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int sum = 0;
        int mn = 101; 
        for (int i = 0; i < 7; i++) {
            int x;
            cin >> x;
            if (x % 2 == 0) {
                sum += x;
                if (x < mn) mn = x;
            }
        }

        cout << sum << ' ' << mn << '\n';
    }

    return 0;
}
