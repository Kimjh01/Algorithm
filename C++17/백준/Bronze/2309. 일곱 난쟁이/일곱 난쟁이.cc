#include <iostream>
#include <algorithm> 
using namespace std;

int main() {
    int h[9], total = 0;

    for (int i = 0; i < 9; i++) {
        cin >> h[i];
        total += h[i];
    }

    int out1 = -1, out2 = -1;

    for (int i = 0; i < 9 && out1 == -1; i++) {
        for (int j = i + 1; j < 9; j++) {
            if (total - h[i] - h[j] == 100) {
                out1 = i;
                out2 = j;
                break;
            }
        }
    }

    int result[7], idx = 0;
    for (int i = 0; i < 9; i++) {
        if (i != out1 && i != out2) {
            result[idx++] = h[i];
        }
    }

    sort(result, result + 7);

    for (int i = 0; i < 7; i++)
        cout << result[i] << "\n";

    return 0;
}