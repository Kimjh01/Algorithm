#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    double r;
    cin >> r;
    cout << fixed << setprecision(6);
    cout << acos(-1.0) * r * r << endl;
    cout << 2.0 * r * r << endl;
    return 0;
}