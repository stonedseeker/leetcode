from collections import Counter

class Solution:
    def topK(self, nums, k):
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n,c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def top_K_elements(self, nums, k):
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append((-c, -n))  # Store tuples with negative frequencies and elements

        res = []

        for i in range(len(freq) - 1, 0, -1):
            freq[i].sort()  # Sort tuples based on frequency and element
            for _, n in freq[i]:
                res.append(-n)  # Append negative element to get the original element
                if len(res) == k:
                    return res
    
    def usingCounter(self, nums, k):
        freq_count = Counter(nums)
        
        # Sort elements based on frequency and then value
        sorted_nums = sorted(freq_count.keys(), key=lambda x: (-freq_count[x], x))
        
        # Return the top k elements
        return sorted_nums[:k]
    


print(Solution().usingCounter([1,1,2,2,3,3,3,4], 2))
