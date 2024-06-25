# class Solution:
#     def generate_results(self, s: str):
#         lst = []
#         res  = []
#
#         def dfs(index, str, lst, res, plusCount):
#             if index == len(str) and plusCount < len(str) - 1:
#                 res.append(lst.copy())
#                 return
#
#             for i in range(plusCount):
#                 lst.append(str[])
#
#
#         dfs(0, str, lst, res, 0)


class Solution:
    def generate_results(self, s: str) -> int:
        def dfs(index, path, curr_sum, prev_num):
            # If we have reached the end of the string, add the current sum to the result
            if index == len(s):
                res.append(curr_sum)
                return
            
            for i in range(index, len(s)):
                # Take the current substring
                num_str = s[index:i+1]
                print(num_str)
                num = int(num_str)
                
                # For the first number, we directly take it as part of the current path
                if index == 0:
                    dfs(i + 1, num_str, num, num)
                else:
                    # Otherwise, we add the current number to the path with a '+'
                    dfs(i + 1, path + '+' + num_str, curr_sum + num, num)

        res = []
        dfs(0, "", 0, 0)
        return sum(res)

# Example usage:
solution = Solution()
print(solution.generate_results("125"))  # Output: 176
print(solution.generate_results("9999999999"))  # Output: 12656242944

