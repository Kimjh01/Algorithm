#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string ciphertext;
    cin >> ciphertext;

    vector<pair<string,string>> schools = {
        {"NLCS","North London Collegiate School"},
        {"BHA","Branksome Hall Asia"},
        {"KIS","Korea International School"},
        {"SJA","St. Johnsbury Academy"}
    };

    for (auto &kv : schools) {
        string key = kv.first;
        string v = kv.second;
        string temp;
        for (char c : v) {
            if ((int)temp.size() == 10) break;
            if (!isalpha((unsigned char)c)) continue;
            if (isupper((unsigned char)c)) temp.push_back((char)tolower((unsigned char)c));
            else temp.push_back(c);
        }
        for (int shift = 0; shift < 26; shift++) {
            string formed;
            formed.reserve(10);
            for (char ch : temp) {
                int x = (ch - 'a' + shift) % 26;
                formed.push_back((char)('a' + x));
            }
            if (formed == ciphertext) {
                cout << key;
                return 0;
            }
        }
    }
    return 0;
}
