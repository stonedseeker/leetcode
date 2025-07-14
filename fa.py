from typing import List

def max_books_after_spell(N: int, C: List[int], B: List[int]) -> int:
    if N < 2 or N > 10**5 or len(C) != N or len(B) != N:
        raise ValueError("Invalid input: N must be between 2 and 10^5, and C and B must have length N")
    
    if any(c < 1 or c > 10**9 for c in C):
        raise ValueError("Invalid input: All capacities must be between 1 and 10^9")
    
    if any(b < 0 or b > c for b, c in zip(B, C)):
        raise ValueError("Invalid input: Books must not exceed capacity and must be non-negative")

    total_books = sum(B)
    max_books = 0

    for start in range(N):
        books = 0
        for i in range(N):
            shelf = (start + i) % N
            space = C[shelf] - books
            if space > 0:
                books += min(space, B[shelf])
            max_books = max(max_books, books)
        
        if max_books == total_books:
            break

    return max_books

# Test cases
print("Testcase 1:", max_books_after_spell(4, [5, 4, 3, 6], [2, 1, 3, 2]))
print("Testcase 2:", max_books_after_spell(3, [7, 8, 9], [4, 5, 6]))
print("Testcase 3:", max_books_after_spell(5, [11, 13, 14, 12, 10], [3, 4, 5, 2, 1]))
print("Testcase 4:", max_books_after_spell(6, [7, 6, 8, 5, 9, 4], [2, 3, 4, 1, 5, 2]))
print("Testcase 5:", max_books_after_spell(4, [10, 40, 30, 20], [5, 15, 12, 8]))

# Exception handling test cases
try:
    print("Exception testcase 1:", max_books_after_spell(1, [5], [3]))
except ValueError as e:
    print("Exception testcase 1 (Expected):", str(e))

try:
    print("Exception testcase 2:", max_books_after_spell(3, [5, 4, 3], [2, 5, 1]))
except ValueError as e:
    print("Exception testcase 2 (Expected):", str(e))

print("Testcase 6:", max_books_after_spell(7, [3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7]))
print("Testcase 7:", max_books_after_spell(3, [1000000000, 1000000000, 1000000000], [333333333, 333333333, 333333334]))
