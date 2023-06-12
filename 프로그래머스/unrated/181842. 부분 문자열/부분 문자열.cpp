#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string str1, string str2) {
    int i,j=0;
    for (int i=0; i < str2.length(); i++) {
        bool flag = true;
        for (int j=0; j<str1.length(); j++) {
            if (str1[j] != str2[i+j]) {
                flag=false;
                break;      
            };
        };
        if (flag) return 1;
    };
    return 0;
};