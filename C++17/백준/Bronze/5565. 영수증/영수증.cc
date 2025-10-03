#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long total, x, sum = 0;
    cin >> total;
    for (int i = 0; i < 9; ++i) { 
        cin >> x; sum += x; 
    }
    cout << (total - sum) << '\n';
    return 0;
}
