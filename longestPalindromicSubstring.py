

def longestPalindrome(s: str) -> str:
    newStr = ""

    palindromes = []

    for i in range(len(s)):
        newStr = s[i]
        for j in range(i, len(s)):
            if i != j:
                newStr += s[j]
                #print(newStr)
                if checkPalindrome(newStr):
                    palindromes.append(newStr)
    print(palindromes)
    
    return max(palindromes) if len(palindromes) > 0 else "empty"


def checkPalindrome(str) :
        l = 0
        r = len(str) - 1

        while l <= r:
            if str[l] == str[r]:
                l += 1
                r -= 1
            else:
                return False

        return True

print(checkPalindrome("malayalam"))

print(longestPalindrome("babad"))

print(longestPalindrome(""))
