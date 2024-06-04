def tri(n):
    lst = []
    for i in range(n):
        lst = []
        for j in range(i+1):
            lst.append(1 + j)
            print(lst)
    return lst

print(tri(4))
            
