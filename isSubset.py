def isSubset( a1, a2, n, m):
    
    dir = {}
    freq_dict = {}

    for val in a1:
        dir[val] = a1.count(val)


    for val in a1:
        freq_dict[val] = freq_dict.get(val, 0) + 1

    print(dir, "\n", freq_dict, end = " ")

    for val in a2:
        if val not in dir or val or dir[val] <= 0:
            return "No"
        dic[val] -= 1
    return "True"




n, m = 5, 2

#nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
#nums2 = [1, 2, 3, 1]


nums1 = [589, 5847 ,595, 959, 258]
nums2 = [258, 25]

print(isSubset(nums1, nums2, n, m))
