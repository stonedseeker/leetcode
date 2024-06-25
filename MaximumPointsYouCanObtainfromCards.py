from types import MappingProxyType
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        lsum = 0
        rsum = 0
        max_sum = []

        for i in range(k):
            print(i, cardPoints[k-1-i::-1], sep = ' ')
            
            lsum = sum(cardPoints[k-i -1::-1])

            rsum = sum(cardPoints[len(cardPoints) -1: k:-1])
            max_sum.append((lsum, rsum, lsum + rsum))

        return max_sum
cardPoints = [1,2,3,4,5,6,1] 
k = 3

print(Solution().maxScore(cardPoints, k))
