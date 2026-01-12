#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long A, B, C, D, E, F, G, H;
    cin >> N >> A >> B >> C >> D >> E >> F >> G >> H;

    int cnt = 0;
    int ansX = 0, ansY = 0, ansZ = 0;

    for (int X = 0; X <= N; X++) {
        for (int Y = 0; Y <= N - X; Y++) {
            int Z = N - X - Y;

            if (A*X + B*Y + C*Z == D &&
                E*X + F*Y + G*Z == H) {

                cnt++;
                if (cnt == 1) {
                    ansX = X;
                    ansY = Y;
                    ansZ = Z;
                } else {
                    cout << 1 << "\n";
                    return 0;
                }
            }
        }
    }

    if (cnt == 0) {
        cout << 2 << "\n";
    } else {
        cout << 0 << "\n";
        cout << ansX << " " << ansY << " " << ansZ << "\n";
    }

    return 0;
}
