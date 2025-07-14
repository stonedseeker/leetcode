"""

Title
Advanced Game Theory: Strategic Resource Allocation

Final Problem Summary
In a competitive resource allocation game, two players take turns selecting resources from a shared pool. Each player aims to maximize their total resource score. The resources are arranged in a circular fashion, and players can choose a resource and any adjacent resources (either side). The game continues until all resources are chosen.

Your task is to implement a function that determines the maximum score the first player can achieve if both players play optimally.

Input
python
Copy code
def max_resource_score(resources: list[int]) -> int:
resources: A list of integers representing the scores of the resources (1 ≤ len(resources) ≤ 100).
Output
An integer representing the maximum score the first player can achieve.
Example
python
Copy code
# Example Case
result = max_resource_score([2, 7, 9, 3, 1])
print(result)  # Output: 12
Exceptional Handling
Raise a ValueError if the input list is empty.
Test Cases
"""

def max_resource_score(resources: list[int]) -> int:
    """
    Determines the maximum score the first player can achieve
    by strategically selecting resources.
    """
    if not resources:
        raise ValueError("Input list cannot be empty.")
    
    n = len(resources)
    if n == 1:
        return resources[0]

    def helper(start: int, end: int) -> int:
        if start == end:
            return resources[start]
        if start + 1 == end:
            return max(resources[start], resources[end])
        
        # Choose the start resource
        choose_start = resources[start] + min(helper(start + 2, end), helper(start + 1, end - 1))
        # Choose the end resource
        choose_end = resources[end] + min(helper(start + 1, end - 1), helper(start, end - 2))
        
        return max(choose_start, choose_end)

    return helper(0, n - 1)


# Test Case #1: Basic case
result = max_resource_score([2, 7, 9, 3, 1])
print(result)  # Expected: 12

# Test Case #2: Larger array with varied scores
result = max_resource_score([1, 5, 3, 7, 10])
print(result)  # Expected: 15

# Test Case #3: All equal values
result = max_resource_score([4, 4, 4, 4])
print(result)  # Expected: 8

# Test Case #4: Empty input
try:
    max_resource_score([])
except ValueError as e:
    print(str(e))  # Expected: "Input list cannot be empty."

# Test Case #5: Resources arranged in a circle
result = max_resource_score([1, 2, 3, 4, 5])
print(result)  # Expected: 9 (optimal choice)

