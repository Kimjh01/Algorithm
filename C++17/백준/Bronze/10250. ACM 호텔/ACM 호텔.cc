#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T; 
    cin >> T;
    while (T--) {
        int H, W, N; 
        cin >> H >> W >> N;
        int Y = (N-1) % H + 1;
        int X = (N-1) / H + 1;
        cout << Y * 100 + X << '\n';
    }
    return 0;
}