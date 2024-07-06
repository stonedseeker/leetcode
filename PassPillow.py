class Solution:
    def passThePillow(self, n: int, t: int) -> int:

        res = 0

        for i in range(n):
            if i <= t:
                res += 1
                t -= 1

        print(res)

        for i in range(n, -1, -1):
            if t == 0:
                return i
            res -= 1
            t -= 1
        return res

print(Solution().passThePillow(9, 4))


# 1   1   1   1
#
# 0   1   2   3
#     5   4
