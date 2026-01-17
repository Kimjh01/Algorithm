#include <iostream>
#include <set>

using namespace std;

int main() {
    char owner;
    cin >> owner;
    
    int N;
    cin >> N;
    
    set<char> history;
    history.insert(owner);
    
    for(int i=0; i<N; ++i){
        char w, l;
        cin >> w >> l;
        if(l == owner){
            owner = w;
            history.insert(owner);
        }
    }
    
    cout << owner << "\n" << history.size();
    
    return 0;
}