#include <string>
#include <vector>
#include <iostream>
#include <typeinfo>

using namespace std;

string solution(string rny_string) {
    string res = "";
    for (int i = 0; i < rny_string.length(); i++) {
        // cout << rny_string[i] << " " << typeid(rny_string[i]).name() << endl;
        if (rny_string[i] == 'm') {
            res += "rn";
        } else {
            res += rny_string[i];
        };
    };
    return res;
};