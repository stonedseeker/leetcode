from collections import defaultdict

class Solution:
    def isTrue(self, s: str) -> bool:
        i = 99
        print(chr(97))
        dir = defaultdict(str)

        for i in range(97, 97+26):
            dir[chr(i)] = 0

        for i in s:
            dir[i] = dir.get(i, 0) + 1
        for i in range(97, 97 + 26):
            if (dir[chr(i)] == 0):
                return False

        print(dir)
        return True



print(Solution().isTrue("The quick brown fox jumps over the lazy dog"))
