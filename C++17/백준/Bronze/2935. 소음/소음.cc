#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string A, op, B;
    cin >> A >> op >> B;

    if (op == "*") {
        cout << "1";
        for (int i = 0; i < A.length() + B.length() - 2; i++) 
            cout << "0";
    } else {
        if (A.length() < B.length()) 
            swap(A, B);
        if (A.length() == B.length()) {
            A[0] = '2';
            cout << A;
        } else {
            A[A.length() - B.length()] = '1';
            cout << A;
        }
    }
    return 0;
}