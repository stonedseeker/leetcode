import numpy as np

numbers = []
with open('day1Input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            line_nums = []
            for v in line:
                # print(v)
                if v.isnumeric():
                    line_nums.append(int(v))
            numbers.append(line_nums)

print(numbers)
two_digit_nums = [n[0]*10 + n[-1] for n in numbers]
result = np.sum(two_digit_nums)
print(result)

#part two
import re

numbers = []
lines = []
with open('day1Input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            line_words = re.findall(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))', line)
            # new_line_words = []
            # for lw in line_words:
            #     if lw == 'twoone':
            #         new_line_words.append(2)
            #         new_line_words.append(1)
            #     else:
            #         new_line_words.append(lw)
            
            numbers.append(line_words)
            lines.append(line)   
print(numbers)

def text_to_digit(text):
    if text == 'one':
        return 1
    elif text == 'two':
        return 2
    elif text == 'three':
        return 3
    elif text == 'four':
        return 4
    elif text == 'five':
        return 5
    elif text == 'six':
        return 6
    elif text == 'seven':
        return 7
    elif text == 'eight':
        return 8
    elif text == 'nine':
        return 9
    else:
        return int(text)

digit_numbers = []
for l in numbers:
    first = l[0]
    last = l[-1]
    if first.isnumeric():
        last = text_to_digit(last)
    elif last.isnumeric():
        first = text_to_digit(first)
    elif not first.isnumeric() and not last.isnumeric():
        first = text_to_digit(first)
        last = text_to_digit(last)
    digit_numbers.append(int(first)*10 + int(last))
print(digit_numbers)
print("ans = ", np.sum(digit_numbers))

print(len(numbers)) 
print(len(digit_numbers))



