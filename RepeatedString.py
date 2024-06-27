

def repeatedString(s, n):
    temp = s
    
    while len(s) < n:
        s += s 
    index = n - len(s)
    
    print(len(s))
    print(s)
    print(index)
    
    for i in range(index):
        s += temp[i]
        print(s)
    
    res = 0
    for i in range(n):
        if s[i] == 'a':
            res += 1
    return res

s, n = "aba", 10

print(repeatedString(s, n))
