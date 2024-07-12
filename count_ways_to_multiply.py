def count(nums, k):
    def dfs(index, current_product, lst, res_set):
        if current_product == k:
            res_set.add(tuple(sorted(lst)))  # Use tuple and sort to ensure uniqueness
            return 
        if current_product > k or index == len(nums):
            return 
        
        # Include the current number
        lst.append(nums[index])
        dfs(index + 1, current_product * nums[index], lst, res_set)
        lst.pop()
        
        # Exclude the current number
        dfs(index + 1, current_product, lst, res_set)

    res_set = set()
    dfs(0, 1, [], res_set)  # Start DFS with product 1
    
    print(res_set)  # Print the unique combinations
    return len(res_set) if 1 not in nums else len(res_set) - 1

# Test Cases
nums = [1, 2, 3, 6]
print(count(nums, 6))  # Expected output: 4

print(count([3, 6, 2, 9, 2], 18))    # Expected output: 2
print(count([3, 6, 2, 9, 3, 2], 36)) # Expected output: 3
print(count([5, 5, 2, 4, 7, 6, 28], 840)) # Expected output: 2

