#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, min = 1000000, max = -1000000;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
        if (arr[i] < min)
            min = arr[i];
        if (arr[i] > max)
            max = arr[i];
    }

    cout << min << ' ' << max;
    return 0;
}
