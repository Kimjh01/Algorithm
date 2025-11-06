#include<iostream>

using namespace std;

int main() {
	int burger = 2000, drink = 2000,  temp = 0;

	for (int i = 0; i <= 2; i++) {
		cin >> temp;
		if (burger >= temp){
			burger = temp;
		}
	}

	for (int i = 0; i <= 1; i++) {
		cin >> temp;
		if (drink >= temp){
			drink = temp;
		}
	}
	cout << (drink + burger-50);
	return 0;
}