#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    getline(cin, s);
    
    int happy = 0, sad = 0;
    for (int i = 0; i + 2 < s.length(); i++) {
        if (s.substr(i, 3) == ":-)") happy++;
        else if (s.substr(i, 3) == ":-(") sad++;
    }

    if (happy == 0 && sad == 0) cout << "none";
    else if (happy == sad) cout << "unsure";
    else if (happy > sad) cout << "happy";
    else cout << "sad";

    return 0;
}