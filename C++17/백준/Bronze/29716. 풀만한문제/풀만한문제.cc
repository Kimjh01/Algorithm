#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int J, N;
    cin >> J >> N;
    cin.ignore(); 

    int cnt = 0;
    string s;

    for (int i = 0; i < N; i++) {
        getline(cin, s);
        int sum = 0;
        for (char c : s) {
            if ('A' <= c && c <= 'Z') 
                sum += 4;
            else if (('a' <= c && c <= 'z') || ('0' <= c && c <= '9')) 
                sum += 2;
            else if (c == ' ') 
                sum += 1;
           
        }
        if (sum <= J) 
            cnt++;
    }

    cout << cnt << '\n';
    return 0;
}
