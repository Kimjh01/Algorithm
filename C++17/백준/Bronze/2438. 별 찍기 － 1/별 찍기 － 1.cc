#include<iostream>
using namespace std;

int main()
{
	int N, i, j;
    cin >> N;
	for(i = 0; i < N; ++i){
        for(j = 0; j<i+1; ++j){
			cout << "*"; 
        }
        cout << '\n';
	}
	return 0;
}