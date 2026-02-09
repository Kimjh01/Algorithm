#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k; 
    cin >> n >> k;
    string s; 
    cin >> s;
    string res = s.substr(k - 1);
    string sub = s.substr(0, k - 1);
    if ((n - k + 1) % 2 == 1) 
        reverse(sub.begin(), sub.end());
    cout << res << sub;
    return 0;
}