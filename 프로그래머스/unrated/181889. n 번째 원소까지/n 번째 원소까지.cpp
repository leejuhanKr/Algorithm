#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list, int n) {
    vector<int> res;
    for (int idx=0; idx < n; idx++) {
        res.push_back(num_list[idx]);
    };
    return res;
};