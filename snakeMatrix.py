class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here 
        list = []
        for i in range(len(matrix)):
            if not i % 2 :
               for j in range(len(matrix[i])):
                   list.append(matrix[i][j])
            else :
               for j in range(len(matrix[i]) - 1, -1, -1):
                   list.append(matrix[i][j])
                   
        return list


matrix =    [
             [45, 48, 54],
             [21, 89, 87],
             [70, 78, 15]
            ]

print(Solution().snakePattern(matrix))
