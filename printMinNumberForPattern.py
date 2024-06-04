def printMinNumberForPattern(S):
    
        ans = [1]
        for ch in S: 
            if ch == 'I': 
                m = ans[-1]+1
                while m in ans: m += 1
                ans.append(m)
            else: 
                ans.append(ans[-1])
                for i in range(len(ans)-1, 0, -1): 
                    if ans[i-1] == ans[i]: ans[i-1] += 1

        
        return ''.join(map(str, ans))

# Example usage
  # Output: "13254"





S = "IIIIDDDI"

print(printMinNumberForPattern(S))
