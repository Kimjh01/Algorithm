#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    int n;
    cin >> n;

    cout << fixed << setprecision(1);

    while (n--) {
        double a, b;
        cin >> a >> b;
        cout << abs(a - b) << endl;
    }

    return 0;
}