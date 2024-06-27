from typing import List 

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lst = []
        res = []

        def dfs(index, fruits, lst, res):
            if index == len(fruits) or len(set(lst)) >= 2:
                res.append(lst.copy())
                return
            
            lst.append(fruits[index])
            dfs(index + 1, fruits, lst, res)
            #lst.pop(len(lst) - 1)
            #dfs(index + 1, fruits, lst, res)

        dfs(0, fruits, [], res)
        print(res)
        res = [len(x) for x in res]
        return max(res)
fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(Solution().totalFruit(fruits))
