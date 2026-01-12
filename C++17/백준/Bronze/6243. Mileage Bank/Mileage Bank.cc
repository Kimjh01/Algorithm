#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    long long sum = 0;

    while (getline(cin, line)) {
        if (line == "#") break;
        if (line == "0") {
            cout << sum << "\n";
            sum = 0;
            continue;
        }

        string a, b, cls;
        long long miles;
        stringstream ss(line);
        ss >> a >> b >> miles >> cls;

        if (cls == "F") sum += 2 * miles;
        else if (cls == "B") sum += (3 * miles + 1) / 2;
        else sum += max(500LL, miles);
    }

    return 0;
}
