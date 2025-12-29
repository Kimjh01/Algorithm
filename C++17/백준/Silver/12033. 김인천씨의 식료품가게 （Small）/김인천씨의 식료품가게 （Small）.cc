#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        multiset<long long> ms;
        for (int i = 0; i < 2 * N; i++) {
            long long p;
            cin >> p;
            ms.insert(p);
        }

        cout << "Case #" << t << ":";
        while (!ms.empty()) {
            long long discounted = *ms.begin();
            ms.erase(ms.begin());
            long long original = discounted / 3 * 4;
            auto it = ms.find(original);
            if (it != ms.end()) ms.erase(it);
            cout << " " << discounted;
        }
        cout << "\n";
    }
    return 0;
}