#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, count = 0;
    cin >> N;

    for(int i=0; i<N; i++) {
        int D;
        cin >> D;
        if (D % 2 != 0) {
            count++;
        }
    }
    cout << count << endl;

    return 0;
}