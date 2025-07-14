def vybhv_inheritance(values: list[int], N: int, M: int, K: int) -> str:
    # Input validation
    if not isinstance(N, int) or not isinstance(M, int) or not isinstance(K, int) or not all(isinstance(v, int) for v in values):
        raise ValueError("Invalid input")
    
    if M > N:
        raise ValueError("M cannot be greater than N")
    
    # Dynamic Programming approach
    dp = [[[False for _ in range(K)] for _ in range(M + 1)] for _ in range(N + 1)]
    
    # Base case: It is possible to select 0 items with sum 0 (i.e., sum % K == 0)
    dp[0][0][0] = True
    
    for i in range(1, N + 1):
        for j in range(0, M + 1):
            for r in range(K):
                # Option 1: Don't take the current item
                dp[i][j][r] = dp[i - 1][j][r]
                
                # Option 2: Take the current item, if we have enough items left to take
                if j > 0:
                    prev_r = (r - values[i - 1]) % K
                    dp[i][j][r] |= dp[i - 1][j - 1][prev_r]
    
    # The answer is whether it's possible to select exactly M items with sum % K == 0
    return "Possible" if dp[N][M][0] else "Impossible"


# Test Case 1: Basic positive case
values = [3, 7, 2, 8, 10]
N = 5
M = 3
K = 5
assert vybhv_inheritance(values, N, M, K) == "Possible"

# Test Case 2: No valid subset
values = [1, 2, 3, 4, 5]
N = 5
M = 2
K = 6
assert vybhv_inheritance(values, N, M, K) == "Possible"

# Test Case 3: Edge case where all values are the same
values = [5, 5, 5, 5, 5]
N = 5
M = 3
K = 5
assert vybhv_inheritance(values, N, M, K) == "Possible"

# Test Case 4: Smallest input
values = [5]
N = 1
M = 1
K = 5
assert vybhv_inheritance(values, N, M, K) == "Possible"

# Test Case 5: Impossible case
values = [1, 3, 5, 7, 9]
N = 5
M = 4
K = 100
assert vybhv_inheritance(values, N, M, K) == "Impossible"

# Test Case 6: M greater than N (Invalid)
try:
    vybhv_inheritance([1, 2, 3], 3, 4, 5)
except ValueError as e:
    assert str(e) == "M cannot be greater than N"

# Test Case 7: Invalid input type
try:
    vybhv_inheritance([1, 2, 3], "three", 2, 5)
except ValueError as e:
    assert str(e) == "Invalid input"

# Test Case 8: Another basic possible case
values = [9, 7, 12, 6, 3]
N = 5
M = 3
K = 9
assert vybhv_inheritance(values, N, M, K) == "Possible"

# Test Case 9: Sum divisible by K but wrong number of elements
values = [9, 7, 12, 6]
N = 4
M = 2
K = 9
assert vybhv_inheritance(values, N, M, K) == "Possible"

# Test Case 10: M equals N and sum is divisible
values = [3, 9, 12, 6]
N = 4
M = 4
K = 3
assert vybhv_inheritance(values, N, M, K) == "Possible"

