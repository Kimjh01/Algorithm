#include <iostream>

using namespace std;

int main() {
    int A, B, C;
    int D;
    cin >> A >> B >> C >> D;

    int total = A * 3600 + B * 60 + C + D;

    int h = (total / 3600) % 24;
    int m = (total / 60) % 60;
    int s = total % 60;

    cout << h << " " << m << " " << s;

    return 0;
}