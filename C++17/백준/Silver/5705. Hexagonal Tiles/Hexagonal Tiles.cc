#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<long long> nums;
    while (true) {
        long long num;
        if (!(cin >> num)) break;
        if (num == 0) break;
        nums.push_back(num);
    }

    for (long long num : nums) {
        unordered_map<long long, long long> memo;
        memo.reserve(1 << 20);
        memo.max_load_factor(0.7f);

        const long long OFF = 1000000LL;

        auto keyOf = [&](long long n, long long x, long long y) -> long long {
            return ((n + 2LL) << 42) ^ ((x + OFF) << 21) ^ y;
        };

        vector<pair<long long, bool>> st;
        st.reserve(1 << 20);
        long long startKey = keyOf(0, 1, 0);
        st.push_back({startKey, false});

        while (!st.empty()) {
            auto [key, expanded] = st.back();
            st.pop_back();

            if (memo.find(key) != memo.end()) continue;

            long long y = key & ((1LL << 21) - 1);
            long long x = ((key >> 21) & ((1LL << 21) - 1)) - OFF;
            long long n = (key >> 42) - 2LL;

            if (n == -1 || y > (num / 2)) {
                memo[key] = 0;
                continue;
            }
            if (n == num) {
                memo[key] = 1;
                continue;
            }

            if (!expanded) {
                st.push_back({key, true});
                if (n % 2 == 0) {
                    long long k1 = keyOf(n + 1, x - 1, y);
                    long long k2 = keyOf(n + 2, x, y + 1);
                    if (memo.find(k1) == memo.end()) st.push_back({k1, false});
                    if (memo.find(k2) == memo.end()) st.push_back({k2, false});
                } else {
                    long long k1 = keyOf(n + 1, x + 1, y + 1);
                    long long k2 = keyOf(n + 2, x, y + 1);
                    if (memo.find(k1) == memo.end()) st.push_back({k1, false});
                    if (memo.find(k2) == memo.end()) st.push_back({k2, false});
                }
            } else {
                long long res = 0;
                if (n % 2 == 0) {
                    long long k1 = keyOf(n + 1, x - 1, y);
                    long long k2 = keyOf(n + 2, x, y + 1);
                    res = memo[k1] + memo[k2];
                } else {
                    long long k1 = keyOf(n + 1, x + 1, y + 1);
                    long long k2 = keyOf(n + 2, x, y + 1);
                    res = memo[k1] + memo[k2];
                }
                memo[key] = res;
            }
        }

        cout << memo[startKey] << "\n";
    }

    return 0;
}
