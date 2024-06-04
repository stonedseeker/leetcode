from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dir = {}
        for i in nums:
            dir[i] = dir.get(i, 0) + 1
        print(dir)

        pq = []
        
        for key, val in dir.items():
             heapq.heappush(pq, (val * -1, key))

        print(pq)

        ans = []

        for i in range(k):
            ans.append(heapq.heappop(pq)[1])

        return ans

nums = [1,1,1,2,2,3]
print(Solution().topKFrequent(nums, 2))


