# Part 1

import sys
from pathlib import Path
from enum import Enum

sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("test_sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")
sequence_list = [x.split() for x in sequence_list]

OPERATOR_LINE = 3 # Change to 3 for test

TOTAL = 0
for j in range(len(sequence_list[0])):
    if sequence_list[OPERATOR_LINE][j] == "*":
        cnt = 1
    elif sequence_list[OPERATOR_LINE][j] == "+":
        cnt = 0
    for i in range(len(sequence_list) - 1):
        if sequence_list[OPERATOR_LINE][j] == "*":
            # print(int(sequence_list[i][j]))
            cnt *= int(sequence_list[i][j])
        elif sequence_list[OPERATOR_LINE][j] == "+":
            # import pdb; pdb.set_trace()
            # print(sequence_list[i][j])
            cnt += int(sequence_list[i][j])
    TOTAL += cnt

print(TOTAL)
print(TOTAL == 4277556)

# Part 2 - Based on spaces and from left to Right

# data_path = Path(__file__).with_name("test_sequence.txt")
# sequence_list = read_sequence(str(data_path), delimiter="\n")


# print(sequence_list)
# where_to_split = []
# for row in sequence_list: 
#     for pos, char in enumerate(row):
#         if char == " ":
#             where_to_split.append(pos)

# real_split_position = [x for x in set(where_to_split) if where_to_split.count(x) >= 4]
# sequence_list = [x.split() for x in sequence_list]
# TOTAL = 0

# for j in range(len(real_split_position), 0, -1):
#     print(j)
#     if sequence_list[OPERATOR_LINE][j] == "*":
#         cnt = 1
#     elif sequence_list[OPERATOR_LINE][j] == "+":
#         cnt = 0
#     for i in range(len(sequence_list), 0, -1): 
#         if sequence_list[OPERATOR_LINE][j] == "*" and sequence_list[i][j] != " ":
#             cnt *= int(sequence_list[i][j])
#         elif sequence_list[OPERATOR_LINE][j] == "+" and sequence_list[i][j] != " ":
#             cnt += int(sequence_list[i][j])
#         print(sequence_list[i][j], cnt)
#     TOTAL += cnt 


from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")

# DON'T split! Keep original spacing
OPERATOR_LINE = len(sequence_list) - 1

# Find columns that are completely empty (separators between problems)
def find_separator_columns(lines):
    max_len = max(len(line) for line in lines)
    separators = []
    for col in range(max_len):
        is_separator = True
        for row_idx in range(len(lines) - 1):  # Check all rows except operator
            if col < len(lines[row_idx]) and lines[row_idx][col] != ' ':
                is_separator = False
                break
        if is_separator:
            separators.append(col)
    return separators

separators = find_separator_columns(sequence_list)
print(f"Separator columns: {separators}")

# Split into problem regions based on separators
problem_regions = []
start = 0
for sep in separators:
    if sep > start:
        problem_regions.append((start, sep))
    start = sep + 1
if start < len(sequence_list[0]):
    problem_regions.append((start, len(sequence_list[0])))

print(f"Problem regions: {problem_regions}")

# Process each problem RIGHT-TO-LEFT
TOTAL = 0
for start_col, end_col in problem_regions:
    # Find operator in this region
    operator = None
    for col in range(start_col, end_col):
        if col < len(sequence_list[OPERATOR_LINE]):
            char = sequence_list[OPERATOR_LINE][col]
            if char in ['*', '+']:
                operator = char
                break
    
    if not operator:
        continue
    
    print(f"\nProcessing problem from columns {start_col} to {end_col}, operator: {operator}")
    
    # Read RIGHT-TO-LEFT, each column is one number read TOP-TO-BOTTOM
    numbers = []
    for col in range(end_col - 1, start_col - 1, -1):  # Right to left
        # Read this column top-to-bottom to build one number
        digits = []
        for row in range(OPERATOR_LINE):  # All rows except operator row
            if col < len(sequence_list[row]):
                char = sequence_list[row][col]
                if char.isdigit():
                    digits.append(char)
        
        if digits:
            number = int(''.join(digits))
            numbers.append(number)
            print(f"  Column {col}: {''.join(digits)} = {number}")
    
    # Apply operator
    if operator == '*':
        result = 1
        for num in numbers:
            result *= num
    else:  # '+'
        result = sum(numbers)
    
    print(f"  Result: {' {} '.format(operator).join(map(str, numbers))} = {result}")
    TOTAL += result

print(f"\nGrand Total: {TOTAL}")

    
    

# import pdb; pdb.set_trace()