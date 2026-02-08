#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long Fs, Cs, Es, Bs;
    long long Fn, Cn, En, Bn;
    cin >> Fs >> Cs >> Es >> Bs;
    cin >> Fn >> Cn >> En >> Bn;
    int Q;
    cin >> Q;

    long long cookie = 0;
    while (Q--) {
        long long q, i;
        cin >> q >> i;
        if (q == 1) {
            long long mx = min({Fs / Fn, Cs / Cn, Es / En, Bs / Bn});
            if (mx >= i) {
                Fs -= Fn * i;
                Cs -= Cn * i;
                Es -= En * i;
                Bs -= Bn * i;
                cookie += i;
                cout << cookie << "\n";
            } else {
                cout << "Hello, siumii\n";
            }
        } else if (q == 2) {
            Fs += i;
            cout << Fs << "\n";
        } else if (q == 3) {
            Cs += i;
            cout << Cs << "\n";
        } else if (q == 4) {
            Es += i;
            cout << Es << "\n";
        } else if (q == 5) {
            Bs += i;
            cout << Bs << "\n";
        }
    }
    return 0;
}
