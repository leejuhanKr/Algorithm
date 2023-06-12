#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int start, int end) {
    int end_idx = end-start;
    vector<int> res(end_idx+1);
    for (int tmp=0; tmp <= end_idx; tmp++) {
        res[tmp] = start + tmp;
    };
    return res;
};