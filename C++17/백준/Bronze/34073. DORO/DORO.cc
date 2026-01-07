#include <iostream>
#include <string>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        cout << s << "DORO" << (i == n - 1 ? "" : " ");
    }
    cout << endl;
    return 0;
}