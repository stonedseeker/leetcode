from collections import Counter

class Solution:
    def shff(self, s: str, t: str):
        temp_s = sorted(s)
        temp_t = sorted(t)

        for i, j in zip(temp_s, temp_t):
            if i != j:
                return j
        return temp_t[-1]


s = "string"
t = "rtingsa"

print(Solution().shff(s, t))
