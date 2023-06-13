#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer = num_list;
    int end_idx = num_list.size()-1;
    int prev_end_idx = end_idx - 1;
    
    if (num_list[end_idx] > num_list[prev_end_idx]) {
        answer.push_back(num_list[end_idx] - num_list[prev_end_idx]);
    } else {
        answer.push_back(answer.back() * 2);
    };
    return answer;
}