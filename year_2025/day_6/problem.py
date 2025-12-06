# Part 1

import sys
from pathlib import Path
from enum import Enum

sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("test_sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")

import pdb; pdb.set_trace()

OPERATOR_LINE = 3

class OPERATORS(Enum)
    

for i in range(len(sequence_list[0])):
    for j in range(sequence_list):
