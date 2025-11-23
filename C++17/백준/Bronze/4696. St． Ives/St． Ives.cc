#include <bits/stdc++.h>
using namespace std;

int main() {
    double a;
    while (true) {
        if (!(cin >> a)) 
            break;
        if (a == 0.0) 
            break;

        double s = 1 + a + pow(a, 2) + pow(a, 3) + pow(a, 4);
        printf("%.2f\n", s);  
    }
    return 0;
}
