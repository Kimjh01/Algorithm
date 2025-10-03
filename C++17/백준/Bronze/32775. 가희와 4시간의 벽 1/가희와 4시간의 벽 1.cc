#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long S, F;
    if (!(cin >> S >> F)) 
        return 0;
    if (S > F) 
        cout << "flight\n";
    else       
        cout << "high speed rail\n";
    return 0;
}
