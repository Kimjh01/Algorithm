#include <iostream>
#include <string>
#include <cctype>   

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;           

        for (char &ch : s) {
            ch = tolower(static_cast<unsigned char>(ch));
        }

        cout << s << '\n';
    }

    return 0;
}
