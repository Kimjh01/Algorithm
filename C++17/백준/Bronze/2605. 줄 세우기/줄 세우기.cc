#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, num;
    cin >> N;
    vector<int> line;

    for (int i = 0; i < N; i++) {
        cin >> num;
        line.insert(line.begin() + (i - num), i + 1);
    }

    for (int x : line) cout << x << " ";
}
