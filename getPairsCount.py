from collections import defaultdict

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        freq_map = defaultdict(int)
        count = 0 
        for num in arr:
            complement = k - num
            count += freq_map[complement]
            freq_map[num] += 1
            print(freq_map)
            print(count)
        return count

n, k = 4, 6

lst = [1, 5, 7, 1]
print(Solution().getPairsCount(lst, n,k))
