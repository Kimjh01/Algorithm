#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long x, N;
    if (!(cin >> x >> N)) 
        return 0;

    for (long long i = 0; i < N; ++i) {
        if (x % 2 == 0) 
            x = (x / 2) ^ 6;   
        else            
            x = (x * 2) ^ 6;  
    }
    cout << x << '\n';
    return 0;
}
