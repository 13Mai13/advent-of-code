# Part 1 

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")
sequence_list = [seq.split(',') for seq in sequence_list]

def calculate_rectangle_area(p1, p2):
    width = abs(int(p1[0]) - int(p2[0])) + 1
    height = abs(int(p1[1]) - int(p2[1])) + 1
    return width * height

LARGEST_AREA = 0

for i in range(len(sequence_list)):
    for i_ad in range(i+1, len(sequence_list)):
        if sequence_list[i][0] != sequence_list[i_ad][0] and sequence_list[i][1] != sequence_list[i_ad][1]:
            area = calculate_rectangle_area(sequence_list[i], sequence_list[i_ad])
            if area > LARGEST_AREA:
                LARGEST_AREA = area

print(f'Largest area is: {LARGEST_AREA}')

