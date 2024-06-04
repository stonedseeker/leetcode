from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:

        map = defaultdict()
        
        for i in s:
            if i in map:
                map[i] += 1
            else: map[i] = 1

        print(map)

        mx = 0
        key = ''
    
        str = ""

        x = map.items();

        for k,v in map.copy().items():
        
            for k,v in map.items():
                if v > mx:
                    max = v
                    key = k

            if key in map:
                s += k * mx
                map.pop(key)


        return s:


print(Solution()frequencySort("tree"))
