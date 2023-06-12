#include <string>
#include <vector>

using namespace std;

string solution(string myString) {
    for (int idx=0; idx < myString.length(); idx++) {
        char chr = myString[idx];
        if ('a' <= chr && chr <= 'z') {
            myString[idx] = chr - 'a' + 'A';
        };
    };
    return myString;
}