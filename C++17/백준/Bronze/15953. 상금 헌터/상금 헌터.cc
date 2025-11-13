#include <bits/stdc++.h>
using namespace std;

int getPrize1(int rank) {
    if (rank == 0) return 0;
    int people[] = {1, 2, 3, 4, 5, 6};
    int money[]  = {500, 300, 200, 50, 30, 10};

    int sum = 0;
    for (int i = 0; i < 6; i++) {
        sum += people[i];
        if (rank <= sum) return money[i];
    }
    return 0;
}

int getPrize2(int rank) {
    if (rank == 0) return 0;
    int people[] = {1, 2, 4, 8, 16};
    int money[]  = {512, 256, 128, 64, 32};

    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += people[i];
        if (rank <= sum) return money[i];
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int a, b;
        cin >> a >> b;

        int prize = getPrize1(a) + getPrize2(b); 
        cout << prize * 10000 << "\n";          
    }
    return 0;
}
