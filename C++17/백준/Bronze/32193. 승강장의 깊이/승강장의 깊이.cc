#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    int depth = 0;  

    while (N--) {
        long long A, B;
        cin >> A >> B;

        depth += (A - B);  
        cout << depth << "\n";
    }

    return 0;
}
