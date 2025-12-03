#include <iostream>
using namespace std;

int cnt[10001]; 

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    int num;
    for (int i = 0; i < N; i++) {
        cin >> num;
        cnt[num]++; 
    }

    for (int i = 1; i <= 10000; i++) {
        for (int j = 0; j < cnt[i]; j++) {
            cout << i << "\n";
        }
    }

    return 0;
}