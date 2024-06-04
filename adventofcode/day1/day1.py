import re
import numpy as np

total_sum = 0
vals = []

dir = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def extract_digits(line):
    numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    # print(numbers)
    
    digits = []
    for num in numbers:
        if num.isdigit():
            digits.append(int(num))
        else:
            digits.append((dir[num]))
    return digits

with open("day1Input.txt", 'r') as file:
    for line in file:       
        line = line.strip()
        if line: 
            digits = extract_digits(line)
            calibration_value = digits[0] * 10 + digits[-1]
            print(calibration_value)
            vals.append(calibration_value)
            
            total_sum += calibration_value
print("Sum of calibration values:", total_sum)
print(" asda00", np.sum(vals))
