from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums  = {0:1}

        cur_sum = 0

        res = 0

        for n in nums:
            cur_sum += n
            diff = cur_sum - k

            res += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)

        return res
