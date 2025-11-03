#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    int n; 
    cin >> n;
    vector<string> v;
    while (n--) { 
        string s; 
        cin >> s; 
        if (s.size()==3) 
            v.push_back(s); 
    }
    cout << *min_element(v.begin(), v.end());
    return 0;
}