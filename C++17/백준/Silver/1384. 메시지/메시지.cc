#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int n, group = 1;
    while (cin >> n && n != 0) {
        if (group > 1) cout << "\n";
        cout << "Group " << group++ << "\n";
        
        vector<string> names(n);
        vector<vector<char>> memo(n, vector<char>(n - 1));
        
        for (int i = 0; i < n; i++) {
            cin >> names[i];
            for (int j = 0; j < n - 1; j++) {
                cin >> memo[i][j];
            }
        }
        
        bool nasty = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (memo[i][j] == 'N') {
                    int sender = (i - (j + 1) + n) % n;
                    cout << names[sender] << " was nasty about " << names[i] << "\n";
                    nasty = true;
                }
            }
        }
        
        if (!nasty) cout << "Nobody was nasty\n";
    }
    return 0;
}