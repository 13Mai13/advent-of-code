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


# Part 2 - The problem is quantum

# timelines = [POSITION_OF_START]

# for row in range(1, len(sequence_list)):
#     next_timelines = []  # Timelines for the next row
    
#     for column in range(len(sequence_list[0])):
#         if sequence_list[row][column] == '^' and column in timelines:
#             # Each timeline at this position splits into two
#             # Count how many timelines are at this column
#             count = timelines.count(column)
#             for _ in range(count):
#                 next_timelines.append(column - 1)  # Left timeline
#                 next_timelines.append(column + 1)  # Right timeline
#         elif column in timelines:
#             # No splitter, timelines continue
#             count = timelines.count(column)
#             for _ in range(count):
#                 next_timelines.append(column)
    
#     timelines = next_timelines  # Update for next row

# # Part 2 answer: total number of timelines
# print(f"Number of timelines: {len(timelines)}")

# Use Counter to track: {column: number_of_timelines_at_that_column}

from collections import Counter

timelines = Counter([POSITION_OF_START])

for row in range(1, len(sequence_list)):
    next_timelines = Counter()
    
    # Only iterate through unique positions (not each timeline)
    for column, count in timelines.items():
        # Check bounds
        if 0 <= column < len(sequence_list[row]):
            if sequence_list[row][column] == '^':
                # All timelines at this position split
                if column - 1 >= 0:
                    next_timelines[column - 1] += count
                if column + 1 < len(sequence_list[row]):
                    next_timelines[column + 1] += count
            else:
                # All timelines continue
                next_timelines[column] += count
    
    timelines = next_timelines

# Total timelines = sum of all counts
print(f"Number of timelines: {sum(timelines.values())}")