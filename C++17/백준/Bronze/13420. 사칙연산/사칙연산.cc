#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while(t--) {
        long long a, b, c, res;
        char op, eq;
        cin >> a >> op >> b >> eq >> c;
        if(op == '+') res = a + b;
        else if(op == '-') res = a - b;
        else if(op == '*') res = a * b;
        else res = a / b;

        if(res == c) cout << "correct\n";
        else cout << "wrong answer\n";
    }
    return 0;
}