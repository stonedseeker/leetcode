
def fibo(n, cache = {}) ->int:
        if n in cache:
            return cache[n]
        if n == 0: 
            return 0 
        
        elif n == 1:
            return 1

        cache[n] =  fibo(n-2, cache) + fibo(n-1, cache)
        return cache[n]

for i in range(10):
    print(i + 1, " ",fibo(i))
