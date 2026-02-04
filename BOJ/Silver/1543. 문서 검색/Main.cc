#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string doc, word;
    getline(cin, doc); getline(cin, word);
    int cnt = 0, pos = 0;
    while ((pos = doc.find(word, pos)) != string::npos) {
        cnt++;
        pos += word.size();
    }
    cout << cnt;
    return 0;
}