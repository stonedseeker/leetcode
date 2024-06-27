


class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def fact(n):
            if n == 0 or n == 1:
                return 1
            return n * fact(n - 1)

        num = fact(n)
        print(num)
        res = 0

        while num:
            rem = num % 10
            if rem != 0:
                break
            if rem == 0:
                res += 1
            num /= 10

        return res

print(Solution().trailingZeroes(30))
        
        
