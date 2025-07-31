#include <iostream>
#include <iomanip> /

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << fixed << setprecision(10) << (double)a / b << endl;
    return 0;
}
