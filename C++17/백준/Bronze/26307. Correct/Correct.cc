#include <iostream>
using namespace std;

int main() {
    int HH, MM;
    cin >> HH >> MM;
    cout << (HH - 9) * 60 + MM;
    return 0;
}
