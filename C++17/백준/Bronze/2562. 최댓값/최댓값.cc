#include <iostream>
using namespace std;

int main() {
    int number, maximum = 0, index = 0;

    for (int i = 1; i <= 9; i++) {
        cin >> number;
        if (number > maximum) {
            maximum = number;
            index = i;  
        }
    }

    cout << maximum << "\n" << index;
    return 0;
}
