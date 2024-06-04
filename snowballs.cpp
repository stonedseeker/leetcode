#include <vector>
using namespace std;
#include <iostream>

class Solution {
public:
  void moveZeroes(vector<int> &nums) {
    int snowBallSize = 0;
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == 0) {
        snowBallSize++;
      } else if (snowBallSize > 0) {
        int t = nums[i];
        nums[i] = 0;
        nums[i - snowBallSize] = t;
      }
    }
  }
};

int main() {
  vector<int> arr{0, 1, 0, 3, 12};
  Solution().moveZeroes(arr);
}
