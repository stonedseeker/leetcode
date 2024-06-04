'''
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

'''

class Solution:
    def count(self, L, R, X):
        # L += 1
        # count = 0
        # while L < R:
        #     temp = str(L)
        # 
        #     if str(X) in temp:
        #         count += 1
        #     L += 1
        #
        #     
        # return count

        L += 1
        
        res = ""
        
        count = 0

        
        while (L < R):
            for j in str(L):
                res += j
                if res[-1] in str(X):
                    count += 1
            L += 1
        return count

print(Solution().count(3, 26, 6))
