def PalinArray(arr ,n):
    # Code here
    for ele in arr:
        if not check(ele):
            return 0
    return 1
    
    
def check(ele):
    ele = str(ele)
    l = 0
    r = len(ele) - 1 
    
    while l <= r:
        if ele[l] == ele[r]:
            l += 1
            r -= 1
        else:
            return False
            
    return True

def is_palindrome(num):
    temp = num
    reverse = 0
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
    return reverse == num

l = [111, 222, 333, 444, 555]
l = [121, 131, 20]
print(PalinArray(l, 5))
