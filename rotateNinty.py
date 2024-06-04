x = [[1,2,3], [4,5,6], [7,8,9]]
res = [[0 for _ in range(len(x[0]))] for i in range(len(x))]

print(len(x), " ", len(res))
print(len(x[0]), " ", len(res[0]))


print(x)


def transpose(x):
    res = [[0 for _ in range(len(x[0]))] for i in range(len(x))]
    for i in range(len(x)):
      for j in range(len(x[0])):
            #print(i, " ", j)
               res[i][j] = x[j][i]

    return res


def rotate(x):
    res = [[0 for _ in range(len(x))] for i in range(len(x[0]))]
  
    for i in range(len(x)):
       for j in range(len(x)):
           res[i][j] = x[i][len(x[0]) - 1 - j]

    return res

    


res = [[0 for _ in range(len(x[0]))] for _ in range(len(x))]

for i in range(len(x)):
    for j in range(len(x[i])):
        res[i][j] = x[len(res) - 1 - j][i]


for row in res:
    print(row)



