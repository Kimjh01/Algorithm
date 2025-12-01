#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int k = n / 3;                 
    long long ans = 1LL * (k - 1) * (k - 2) / 2;
    cout << ans;
    return 0;
}
