#include<iostream>
using namespace std;

int main()
{
	ios::sync_with_stdio(0);
    cin.tie(0);
    int V, E, tc;
    cin >> tc;
    for(int i = 1; i <= tc; i++){
        cin >> V >> E;
        if(V >= E){
            cout << "MMM BRAINS" << "\n";  
        }
        else{
            cout << "NO BRAINS" << "\n";
        }
    }
	return 0;
}