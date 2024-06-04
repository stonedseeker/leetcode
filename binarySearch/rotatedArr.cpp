#include <iostream>
using namespace std;
#include <vector>

class Solution {
public:
  int findMin(vector<int> &nums) {

    int l = 0;
    int r = nums.size() - 1;
    while (l < r) {
      int mid = (l + r) / 2;
      if (nums[mid] > nums[r])
        l = mid + 1;
      else
        r = mid - 1;
    }

    return nums[l];
  }
};

int main() {
  vector<int> vect{3, 1, 2};
  cout << Solution().findMin(vect);
  return 0;
}
