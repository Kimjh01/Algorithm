#include<iostream>
#include<string>

using namespace std;

int main(){
    string sign;
    cin >> sign;
    if(sign == "SONGDO"){
        cout << "HIGHSCHOOL";
    }
    else if(sign == "CODE"){
        cout << "MASTER";        
    }
    else if(sign == "2023"){
        cout << "0611";
    }
    else 
        cout << "CONTEST";

    return 0;
}