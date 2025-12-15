#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<int> h(n);
    for(int i = 0; i < n; i++) cin >> h[i];

    long long min_cost = -1;

    for(int i = 0; i <= 83; i++) {
        int low = i;
        int high = i + 17;
        long long cost = 0;
        for(int x : h) {
            if(x < low) cost += (low - x) * (low - x);
            else if(x > high) cost += (x - high) * (x - high);
        }
        if(min_cost == -1 || cost < min_cost) min_cost = cost;
    }
    cout << min_cost;
    return 0;
}