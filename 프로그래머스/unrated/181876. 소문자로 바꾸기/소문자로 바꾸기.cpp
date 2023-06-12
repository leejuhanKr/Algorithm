#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string myString) {
    for (int idx=0; idx < myString.length(); idx++) {
        char chr = myString[idx];
        if ('A' <= chr && chr <= 'Z') {
            myString[idx] = chr - 'A' + 'a';
        };
    };
    return myString;
}