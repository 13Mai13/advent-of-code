import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter=",")

# Part 1

ADDITION_OF_ALL_INVALID_IDS = 0

for id_range in sequence_list:

    start, end = id_range.split("-")

    for id in range(int(start), int(end) + 1):

        first_half = str(id)[:len(str(id))//2]
        second_half = str(id)[len(str(id))//2:]

        if first_half == second_half:
            ADDITION_OF_ALL_INVALID_IDS += id



print(ADDITION_OF_ALL_INVALID_IDS)
ADDITION_OF_ALL_INVALID_IDS = 0

# Part 2

def check_if_a_pattern_exists(id: int, split_index: int) -> bool:
    parts = [id[i:i+split_index] for i in range(0, len(id), split_index)]
    return len(set(parts)) == 1

for id_range in sequence_list:

    start, end = id_range.split("-")

    for id in range(int(start), int(end) + 1):
        for split_index in range(1, len(str(id))):
            if check_if_a_pattern_exists(str(id), split_index):
                ADDITION_OF_ALL_INVALID_IDS += id
                break

print(ADDITION_OF_ALL_INVALID_IDS)