from collections import Counter

class Solution:
    def frequencyCount(self, arr, N):
        # code here
        frequency_dict = Counter(arr)  # Count frequencies of array elements using Counter

        result = []
        for key, val in frequency_dict:
            result.append(frequency_dict.get(val, 0))  # Get the frequency of num, if not found, default to 0
       
        return result

# Example usage
sol = Solution()
N = 5
arr = [2, 3, 2, 3, 5]
output = sol.frequencyCount(arr, N)
print(" ".join(map(str, output)))  # Output: 2 2 2 2 1


