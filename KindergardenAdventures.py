#!/bin/python3

import os
import sys
from collections import defaultdict
#
# Complete the solve function below.
#
def solve(nums):
    #
    # Return the ID
    #
    

    count = defaultdict(int)
    
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[(i + j) % len(nums)] - i <= j:
                count[i] = count.get(i, 0) + 1
                print(count)

    print(count)
    min = sys.maxsize 

    for i in range(len(count)):
        if count[i] < min:
            min = i 
    return nums[min] + 1


if __name__ == '__main__':
    

    t_count = int(input())

    t = list(map(int, input().rstrip().split()))

    id = solve(t)

    print(id)

