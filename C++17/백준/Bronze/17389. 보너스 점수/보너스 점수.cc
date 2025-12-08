#include <iostream>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;
    string S;
    cin >> S;

    int total_score = 0;
    int bonus = 0;

    for (int i = 0; i < N; i++) {
        if (S[i] == 'O') {
            total_score += (i + 1) + bonus; 
            bonus++;
        } else {
            bonus = 0; 
        }
    }

    cout << total_score << endl;

    return 0;
}