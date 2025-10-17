#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    int a,b,c,d; 
    cin >> a >> b >> c >> d;
    cout << ( ( (a==8||a==9) && (d==8||d==9) && (b==c) ) ? "ignore" : "answer" );
    return 0;
}
