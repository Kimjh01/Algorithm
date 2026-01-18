#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    
    vector<string> grid(n);
    for(int i=0; i<n; ++i) 
    cin >> grid[i];
    
    int valid = 1;
    
    for(int i=0; i<n; ++i){
        int b = 0, w = 0;
        for(int j=0; j<n; ++j){
            if(grid[i][j] == 'B') b++;
            else w++;
            
            if(j >= 2){
                if(grid[i][j] == grid[i][j-1] && grid[i][j-1] == grid[i][j-2]) valid = 0;
            }
        }
        if(b != w) valid = 0;
    }
    
    if(valid){
        for(int j=0; j<n; ++j){
            int b = 0, w = 0;
            for(int i=0; i<n; ++i){
                if(grid[i][j] == 'B') b++;
                else w++;
                
                if(i >= 2){
                    if(grid[i][j] == grid[i-1][j] && grid[i-1][j] == grid[i-2][j]) valid = 0;
                }
            }
            if(b != w) valid = 0;
        }
    }
    
    cout << valid;
    
    return 0;
}