#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	string N;
	cin >> T;
    getline(cin, N);
	for (int i = 1; i <= T; ++i) {
		getline(cin, N);
		cout << i << ". " << N << '\n';
	}

	return 0;
}