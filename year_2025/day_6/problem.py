# Part 1

import sys
from pathlib import Path
from enum import Enum

sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")
sequence_list = [x.split() for x in sequence_list]

OPERATOR_LINE = 4 # Change to 3 for test

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
