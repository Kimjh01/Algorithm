#include <iostream>
#include <algorithm> 
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    while (true) {
        int sides[3];
        cin >> sides[0] >> sides[1] >> sides[2];

        if (sides[0] == 0 && sides[1] == 0 && sides[2] == 0) {
            break;
        }

        sort(sides, sides + 3);

        if (sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2]) {
            cout << "right" << "\n";
        } else {
            cout << "wrong" << "\n";
        }
    }

    return 0;
}