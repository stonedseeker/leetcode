from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res.append(strs[i], " ")
        res = res[:-2]
        print(res)
        return res

    def decode(self, t: str) -> List[str]:
        res = []

        for c in range(len(t)):
            s = ""
            while t[c] != " ":
                s += t[c]
                c += 1
                
            res.append(s)
        print(res)
        return res


Input =  ["neet","code","love","you"]
print(Solution().encode(Solution().decode(Input)))



# Output:[`"neet","code","love","you"]

