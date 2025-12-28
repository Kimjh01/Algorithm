#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        int max_votes = 0, total_votes = 0, winner_idx = 0;
        vector<int> votes(N + 1);
        
        for (int i = 1; i <= N; i++) {
            cin >> votes[i];
            total_votes += votes[i];
            if (votes[i] > max_votes) {
                max_votes = votes[i];
                winner_idx = i;
            }
        }

        int max_count = 0;
        for (int i = 1; i <= N; i++) {
            if (votes[i] == max_votes) max_count++;
        }

        if (max_count > 1) cout << "no winner\n";
        else if (max_votes > total_votes / 2) cout << "majority winner " << winner_idx << "\n";
        else cout << "minority winner " << winner_idx << "\n";
    }
    return 0;
}