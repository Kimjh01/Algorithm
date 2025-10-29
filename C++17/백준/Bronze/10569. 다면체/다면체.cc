#include<iostream>
using namespace std;

int main()
{
	ios::sync_with_stdio(0);
    cin.tie(0);
    int V, E, S, tc;
    cin >> tc;
    for(int i = 1; i <= tc; i++){
        cin >> V >> E;
        S = (V-E-2)*-1;
        cout << S << "\n";
    }
	return 0;
}