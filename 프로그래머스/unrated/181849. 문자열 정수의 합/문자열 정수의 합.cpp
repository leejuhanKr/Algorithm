#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string num_str) {
    int sum = 0;
    for (char name: num_str) {
        sum += name - '0';
    };
    return sum;
}