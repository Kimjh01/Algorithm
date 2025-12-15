#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, d, p;
    cin >> n >> d >> p;
    vector<int> h(n);
    for(int i = 0; i < n; i++) cin >> h[i];

    int turns = 0;
    int i = 0;
    while(i < n) {
        while(h[i] > 0) {
            h[i] -= d;
            turns++;
            if(h[i] < 0 && i + 1 < n) {
                h[i+1] -= (-h[i] * p / 100);
            }
        }
        i++;
    }
    cout << turns;
    return 0;
}