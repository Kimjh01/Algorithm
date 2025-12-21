#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    string S;
    cin >> S;
    int M;
    cin >> M;
    string P;
    cin >> P;

    vector<bool> hasChar(26, false);
    for (char c : S) hasChar[c - 'a'] = true;
    for (char c : P) {
        if (!hasChar[c - 'a']) {
            cout << -1;
            return 0;
        }
    }

    int count = 0;
    int wheelIdx = N - 1; 

    for (char target : P) {
        int steps = 0;
        while (true) {
            wheelIdx = (wheelIdx + 1) % N;
            steps++;
            if (S[wheelIdx] == target) {
                break;
            }
        }
        count += steps;
    }

    cout << count;
    return 0;
}