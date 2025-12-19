#include <iostream>
#include <string>

using namespace std;

int getSum(int n) {
    string s = to_string(n);
    int sum = 0;
    for (char c : s) {
        sum += c - '0';
    }
    return sum;
}

int main() {
    int L, D, X;
    cin >> L >> D >> X;

    for (int i = L; i <= D; ++i) {
        if (getSum(i) == X) {
            cout << i << endl;
            break;
        }
    }

    for (int i = D; i >= L; --i) {
        if (getSum(i) == X) {
            cout << i << endl;
            break;
        }
    }

    return 0;
}