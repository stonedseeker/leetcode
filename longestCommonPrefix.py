from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return "" 
            
        min_str = [x for x in strs if len(x) == min(len(i) for i in strs)]
        print(min_str)
        min_str = min_str[0]
        print(min_str)

        

        res = ""
        for i in range(len(min_str)):
            if all(strs[i]) == min_str[i]:
                print(i)
                res  += min_str[i]

        return res
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))
