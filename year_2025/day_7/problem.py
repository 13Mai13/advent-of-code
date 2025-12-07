from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")



POSITION_OF_START = sequence_list[0].index('S')

NUMBER_OF_SPLITS = 0

POSITIONS_TO_SPLIT = []

POSITIONS_TO_SPLIT.append(POSITION_OF_START)


for row in range(1, len(sequence_list)):
    next_positions = []  # New beams for the next row
    
    for column in range(len(sequence_list[0])):
        if sequence_list[row][column] == '^' and column in POSITIONS_TO_SPLIT:
            NUMBER_OF_SPLITS += 1
            next_positions.append(column - 1)  # Left Split
            next_positions.append(column + 1)  # Right Split
            # Don't add column itself (beam stops)
        elif column in POSITIONS_TO_SPLIT:
            # No splitter, beam continues
            next_positions.append(column)
    
    POSITIONS_TO_SPLIT = next_positions  # Update for next row 

print(NUMBER_OF_SPLITS)