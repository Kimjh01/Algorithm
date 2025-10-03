#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long a1,b1,c1,d1,e1, a2,b2,c2,d2,e2;
    cin >> a1 >> b1 >> c1 >> d1 >> e1;
    cin >> a2 >> b2 >> c2 >> d2 >> e2;
    auto score = [](long long t,long long f,long long s,long long p1,long long p2){
        return 6*t + 3*f + 2*s + 1*p1 + 2*p2;
    };
    cout << score(a1,b1,c1,d1,e1) << ' ' << score(a2,b2,c2,d2,e2) << '\n';
    return 0;
}
