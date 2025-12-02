#include <iostream>
using namespace std;

int main() {
    unsigned int N;
    cin >> N;

    unsigned int rev = 0;
    while (N > 0) {
        rev = (rev << 1) | (N & 1);  // rev = rev*2 + (N%2)
        N >>= 1;
    }

    cout << rev;
    return 0;
}
