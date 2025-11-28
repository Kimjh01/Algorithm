#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    bool ok = true;
    for (int i = 0; i < (int)s.size() / 2; i++) {
        if (s[i] != s[s.size() - 1 - i]) {
            ok = false;
            break;
        }
    }

    cout << (ok ? 1 : 0);
    return 0;
}
