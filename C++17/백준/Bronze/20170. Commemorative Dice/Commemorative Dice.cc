#include <iostream>
#include <numeric>
using namespace std;

int main() {
    int a[6], b[6];
    for (int i = 0; i < 6; i++) cin >> a[i];
    for (int i = 0; i < 6; i++) cin >> b[i];

    int win = 0;
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 6; j++) {
            if (a[i] > b[j]) win++;
        }
    }

    int total = 36;
    int common = std::gcd(win, total);
    cout << win / common << "/" << total / common;

    return 0;
}