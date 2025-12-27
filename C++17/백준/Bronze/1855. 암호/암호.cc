#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int K;
    string S;
    cin >> K >> S;
    int R = S.length() / K;
    vector<vector<char>> grid(R, vector<char>(K));

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < K; j++) {
            if (i % 2 == 0) grid[i][j] = S[i * K + j];
            else grid[i][K - 1 - j] = S[i * K + j];
        }
    }

    for (int j = 0; j < K; j++) {
        for (int i = 0; i < R; i++) {
            cout << grid[i][j];
        }
    }
    return 0;
}