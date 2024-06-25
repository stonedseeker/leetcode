from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i = j = 0
        for i, j  in zip(range(len(nums1)), range(len(nums2))):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        print(res)
        if (len(res) % 2):
            return res[len(res) // 2]
        else:
            return (res[len(res) // 2] + res[(len(res) // 2) - 1] / 2)

nums1 = [1, 3]
nums2 = [2]

print(Solution().findMedianSortedArrays(nums1, nums2))
