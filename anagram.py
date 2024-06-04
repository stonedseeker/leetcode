class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        map = {}

        for i in s:
            if i in t:
                continue
            else: return False

        return True



print(Solution().isAnagram("anagram","ngaram"))
