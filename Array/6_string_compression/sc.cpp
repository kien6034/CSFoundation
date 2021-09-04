
#include <iostream>
#include <stdio.h>
#include <string.h>
#include<bits/stdc++.h>

using namespace std;


string compress(string str){
    char pre = str[0];
    int diff = 1, repeat = 1;
    for (int i =1; i< str.length(); i++){
        if (str[i] == pre){
            diff -= 1;
            repeat += 1;
        }
        else{
            if (repeat >= 10){
                diff += 2;
            }
            else{
                diff += 1;
            }
            pre = str[i];
            repeat = 0;
        }
    }
    
    if (diff > 0){
        return str;
    }
    else{
        char compressed_str[str.length() + diff];
        int i, j =1;
        
        char p = str[0];
        int rep = 1;
        compressed_str[0] = p;
        
        compressed_str[1] = (char)rep;
        for (i=1; i < str.length(); i++){
            if (str[i] == p){
                rep += 1;
            }
            else{
                compressed_str[j]= (char)rep;
                cout << rep << endl;
                p = str[i];
                compressed_str[++j] = str[i];
                rep = 1;
                compressed_str[++j] = (char)rep;
            }
        }
        return compressed_str;
    }

}


string getStringInput(){
    char str[256];
    gets( str);

    return str;
}


int main(){
    string str1 = getStringInput();
    
    string compressed_string = compress(str1);
    cout << compressed_string <<endl;
    return 0;
}
