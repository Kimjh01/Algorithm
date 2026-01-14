#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int T;
    cin >> T;
    
    while(T--) {
        long long arr[3];
        long long D;
        cin >> arr[0] >> arr[1] >> arr[2] >> D;
        
        sort(arr, arr+3);
        
        long long diff = arr[2] - arr[1];
        long long cut = min(D, diff);
        arr[2] -= cut;
        D -= cut;
        
        if(D > 0) {
            diff = arr[1] - arr[0];
            long long can_cut = diff * 2;
            if(D >= can_cut) {
                arr[1] = arr[0];
                arr[2] = arr[0];
                D -= can_cut;
            } else {
                long long half = D / 2;
                arr[1] -= half;
                arr[2] -= half;
                if(D % 2 != 0) arr[2]--;
                D = 0;
            }
        }
        
        if(D > 0) {
            long long part = D / 3;
            arr[0] -= part;
            arr[1] -= part;
            arr[2] -= part;
            D %= 3;
            
            while(D > 0) {
                sort(arr, arr+3);
                arr[2]--;
                D--;
            }
        }
        
        cout << arr[0] * arr[1] * arr[2] << "\n";
    }
    return 0;
}