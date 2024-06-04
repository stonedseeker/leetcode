import re

total_sum = 0

dir = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def extract_digits(line):
    numbers = re.findall(r'\d+|one|two|three|four|five|six|seven|eight|nine', line)
    print(numbers)
    
    digits = []
    for num in numbers:
        if num.isdigit():
            digits.extend(map(int, num))
        else:
            digits.extend(map(int, str(dir[num])))

    return digits

with open("day1Input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            digits = extract_digits(line)
            # Always apply the logic for spelled-out numbers
            total_sum += sum(digits)

print("Sum of calibration values:", total_sum)

