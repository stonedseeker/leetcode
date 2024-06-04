

from collections import Counter

n = int(input())

a = list(map(int, input().split()))

print(a)

# Using Counter to count occurrences of each singer
m = Counter(a)

print(m)

cnt = 0
mx = 0

for singer, count in m.items():
    if count == mx:
        cnt += 1
    elif count > mx:
        mx = count
        cnt = 1

print(cnt)

