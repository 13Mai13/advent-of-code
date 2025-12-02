import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("test_sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter=",")

# Problem 1

ADDITION_OF_ALL_INVALID_IDS = 0

for id_range in sequence_list:

    start, end = id_range.split("-")

    for id in range(int(start), int(end) + 1):

        first_half = str(id)[:len(str(id))//2]
        second_half = str(id)[len(str(id))//2:]

        if first_half == second_half:
            ADDITION_OF_ALL_INVALID_IDS += id



print(ADDITION_OF_ALL_INVALID_IDS)