#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    if (N < 60){
      cout << 'F';
    }
    else if (N < 70)
    {
      cout << 'D';
    }
    else if (N < 80)
    {
      cout << 'C';
    }
    else if (N < 90)
    {
      cout << 'B';
    }
    else
      cout << 'A';
    return 0;
}