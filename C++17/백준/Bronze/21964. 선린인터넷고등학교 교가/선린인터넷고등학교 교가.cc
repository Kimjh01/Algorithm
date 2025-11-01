#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    string S;
    cin >> N >> S;                 
    cout << S.substr(N - 5) << '\n'; 
    return 0;
}
