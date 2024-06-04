class Solution:
    def containsDuplicate(self, nums) -> bool:
        lst = []

        for num in nums:
            if num in lst:
                return False
            else: lst.append(num)

    
        return True


print(Solution().containsDuplicate([1,2,3,1]))
