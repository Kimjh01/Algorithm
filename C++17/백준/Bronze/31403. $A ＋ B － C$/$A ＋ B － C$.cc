#include <bits/stdc++.h>
using namespace std;

int main() {
    string a, b;
    long long C;
    cin >> a >> b >> C;
    long long A = stoll(a), B = stoll(b);
    long long temp = stoll(a+b);
    cout << A+B-C << "\n";
    cout <<temp-C;
    return 0;
}
