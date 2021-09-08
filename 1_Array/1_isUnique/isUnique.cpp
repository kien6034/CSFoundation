/*
    Implemenet an algortihm to determine if a string has all unique characters. No additional data strucutre.
*/
#include <iostream>
#include <string.h>

using namespace std;


bool checkUnique(string str){
    
    if (str.length() > 256){
        return false;
    }

    bool checker[256] = {false};

    for (int i = 0; i < str.length(); i ++){
        int ascval = int(str[i]);
        if (checker[ascval]){
            return false;
        }
        else{
            checker[ascval] = true;
        }
    }
    return true;
}

int main(){
    string str= "hello world";
    string str2 = "ab cd ef";
    bool isunique = checkUnique(str);
    bool isunique2 = checkUnique(str2);
    cout << isunique <<endl;
    cout << isunique2 <<endl;
    return 0;
}