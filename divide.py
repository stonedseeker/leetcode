class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for overflow handling
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # Edge case: division by zero
        if divisor == 0:
            raise ValueError("Division by zero is not allowed")
        
        # Edge case: overflow handling
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Convert to positive
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Division using bit shifting
        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        
        if negative:
            quotient = -quotient
        
        return max(MIN_INT, min(MAX_INT, quotient))

# Test cases
sol = Solution()

# Test case 1: Basic division
print(sol.divide(10, 3))  # Expected output: 3

# Test case 2: Negative result
print(sol.divide(7, -3))  # Expected output: -2

# Test case 3: Overflow
print(sol.divide(-2**31, -1))  # Expected output: 2**31 - 1

# Test case 4: Division by zero
try:
    print(sol.divide(1, 0))  # Expected output: ValueError
except ValueError as e:
    print(e)  # Expected output: Division by zero is not allowed
assert(sol.divide(-2**31, 1)==-2**31)
assert(sol.divide(-2**31, -1)==2**31 - 1)
