#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    while (N--) {
        int a_cnt, b_cnt;
        int a[5] = {0}, b[5] = {0};
        
        cin >> a_cnt;
        for (int i = 0; i < a_cnt; i++) {
            int shape; cin >> shape;
            a[shape]++;
        }
        
        cin >> b_cnt;
        for (int i = 0; i < b_cnt; i++) {
            int shape; cin >> shape;
            b[shape]++;
        }

        bool winner = false;
        for (int i = 4; i >= 1; i--) {
            if (a[i] > b[i]) {
                cout << "A\n";
                winner = true;
                break;
            } else if (b[i] > a[i]) {
                cout << "B\n";
                winner = true;
                break;
            }
        }
        if (!winner) cout << "D\n";
    }
    return 0;
}