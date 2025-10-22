#include <iostream>
using namespace std;

int main() {
    int H, M;
    cin >> H >> M;

    if (M < 45) {
        M = M + 60 - 45;
        H--;
        if (H < 0) H = 23;
    } else {
        M -= 45;
    }

    cout << H << " " << M;
    return 0;
}