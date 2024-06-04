class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y):
        
        
        def lcs(X, Y):
            res = ""
            tempY = Y
            for i in X:
                if i in tempY:
                    res += i
                    print("res = ",res, end="\n")

            
            print(res)
            return res
        
        return len(X) + len(Y) - len(lcs(X,Y))



s = "aaaaa"
y = "aa"

print(Solution().shortestCommonSupersequence(s,y))
