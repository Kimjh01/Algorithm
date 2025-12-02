#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    long long c, b;
    cin >> c >> b;

    cout.setf(ios::fixed);
    cout << setprecision(10) << (long double)c / (long double)b;
    return 0;
}
