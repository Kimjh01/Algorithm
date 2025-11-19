#include <iostream>
using namespace std;

int main() {
    long long N, M;
    cin >> N >> M;

    long long diff = N - M;
    if (diff < 0) diff = -diff;  

    cout << diff;
    return 0;
}