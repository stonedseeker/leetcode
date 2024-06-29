from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini, maxi = [x for x in strs if len(x) == min(len(i) for i in strs)], [x for x in strs if len(x) == max(len(i) for i in strs)]
        mini = mini[0]
        maxi = maxi[0]
        print(mini, maxi, sep = ' ')

        mini, maxi = min(strs), max(strs)
        print(mini, maxi, sep = ' ')

        for i in range(len(mini)):
            if mini[i] != maxi[i]:
                return mini[:i]
        return ""

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))
