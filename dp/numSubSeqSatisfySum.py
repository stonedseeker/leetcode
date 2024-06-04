nums = [1,2,3]


dp = [[nums[i] + nums[j] for i in range(len(nums))] for j in range(len(nums))]

print(dp)

print(sum(nums[:]))
