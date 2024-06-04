from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')]+=1
                print(f"count = {count}")

            res[tuple(count)].append(s)
            print(f"res = {res}")

        return res.values()

    def groupAnagrams2(self, strs:List[str]) -> List[List[str]]:
        a = dict()

        for i in strs:
            x = ''.join(sorted(i))
            if x in a:
                a[x].append(i)
            else:
                a[x] = [i]
        return list(a.values())
        

strs = ["tea", "tan", "ate", "nat", "ant"]
print(Solution().groupAnagrams2(strs))
    #res = []

        #map = {}

        #for str in strs:
        #   level = []
        #   if sorted(str) in res:
        #       level.append(str)
        #   res.append(level)
        #   
        #return res
        
#       res = defaultdict(list) #mapping char_count to list of anagrams

#       for str in strs:
#           count = [0] * 26 # a - z
#
#       
#           for c in str:
#               count[ord(c) - ord("a")] += 1
#
#           res[tuple(count)].append(str)
#
        #return res.values()

        # anagram_dict = {}
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     if sorted_s in anagram_dict:
        #         anagram_dict[sorted_s].append(s)
        #     else:
        #         anagram_dict[sorted_s] = [s]
        #
        #
        # print(anagram_dict)
        # 
        # return list(anagram_dict.values())

# l = ["eat","tea","tan","ate","nat","bat"]
# print(Solution().groupAnagrams(l))
