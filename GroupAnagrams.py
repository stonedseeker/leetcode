from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for i in strs:
            
            if ''.join(sorted(i)) in map:
                map[''.join(sorted(i))].append(i)
            else: map[''.join(sorted(i))].append(i)
        return map.values()


strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams(strs))
