/*
   Given 2 strings, write a method to determine if one is permutatation of the other
   #1, 84, 122, 131
*/
#include <iostream>
#include <string.h>
#include<bits/stdc++.h>

using namespace std;

void sortString(string &str){
    sort(str.begin(), str.end());
}

bool isPermutation(string str1, string str2){
    //cout << "2 input string are: " + str1 + "-" + str2<< endl;
    
    if (str1.length() != str2.length()){
        return false;
    }

    for(int i=0; i< str1.length(); i++){
        if (str1[i] != str2[i]){
            return false;
        }
    }
    return true;
}

string getStringInput(){
    string str;
    cout << "Type string: " << endl;
    cin >> str;

    return str;
}

int main(){
    string str1 = getStringInput();
    string str2 = getStringInput();

    sortString(str1);
    sortString(str2);
    
    bool val = isPermutation(str1, str2);
    
    cout << val <<endl;
    return 0;
}

//TODO: using hash table 