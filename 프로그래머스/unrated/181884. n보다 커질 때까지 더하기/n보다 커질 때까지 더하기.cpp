#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers, int limit) {
    int sum = 0;
    for (int n: numbers) {
        if (sum > limit) {
            return sum;
        };
        sum += n;
    };
    return sum;
}