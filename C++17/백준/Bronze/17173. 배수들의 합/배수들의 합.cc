#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> k(m);
    for (int i = 0; i < m; i++) cin >> k[i];

    int sum = 0;
    for (int i = 1; i <= n; i++) {
        bool check = false;
        for (int x : k) {
            if (i % x == 0) {
                check = true;
                break;
            }
        }
        if (check) sum += i;
    }
    cout << sum;
    return 0;
}