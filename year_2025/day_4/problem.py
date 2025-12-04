# Part 1

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("test_sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")

data_path = Path(__file__).with_name("test_sequence_solution.txt")
sequence_list_sol = read_sequence(str(data_path), delimiter="\n")

NUMBER_OF_PAPER_ROLLS = 0


MAX_I = len(sequence_list[0])
MAX_J = len(sequence_list)

## Issues with list -> Probably a better data structure for this

# for i in range(MAX_I):
#     for j in range(MAX_J):
#         if sequence_list[i][j] == '@': 
#             adjacent_positions = []
#             # Check adjacent positions
#             if (i > 0) & (j > 0) & (j < MAX_J) & (i < MAX_I): # No edge cases
#                 adjacent_positions.append(int(bool(sequence_list[i-1][j-1])), int(bool(sequence_list[i-1][j])), int(bool(sequence_list[i-1][j+1])))# Row 1
#                 adjacent_positions.append(int(bool(sequence_list[i][j-1])), int(bool(sequence_list[i][j+1])))# Row 2 
#                 adjacent_positions.append(int(bool(sequence_list[i+1][j-1])), int(bool(sequence_list[i+1][j])), int(bool(sequence_list[i+1][j+1])))# Row 3
#             elif (i == 0) & (j > 0) & (j < MAX_J): 
#                 adjacent_positions.append(int(bool(sequence_list[i][j-1])), int(bool(sequence_list[i][j+1])))# Row 2 
#                 adjacent_positions.append(int(bool(sequence_list[i+1][j-1])), int(bool(sequence_list[i+1][j])), int(bool(sequence_list[i+1][j+1])))# Row 3 
#             elif (i == 0) & (j == MAX_J):
#                 adjacent_positions.append(int(bool(sequence_list[i][j-1])))# Row 2 
#                 adjacent_positions.append(int(bool(sequence_list[i+1][j-1])), int(bool(sequence_list[i+1][j])))# Row 3
#             elif (i == 0) & (j == 0):
#                 adjacent_positions.append(int(bool(sequence_list[i][j+1])))# Row 2 
#                 adjacent_positions.append(int(bool(sequence_list[i+1][j])), int(bool(sequence_list[i+1][j+1])))# Row 3 
#             elif (i == MAX_I) & (j > 0) & (j < MAX_J): 
#                 adjacent_positions.append(int(bool(sequence_list[i-1][j-1])), int(bool(sequence_list[i-1][j])), int(bool(sequence_list[i-1][j+1])))# Row 1
#                 adjacent_positions.append(int(bool(sequence_list[i][j-1])), int(bool(sequence_list[i][j+1])))# Row 2  
#             elif (i == MAX_I) & (j == MAX_J): 
#                 adjacent_positions.append(int(bool(sequence_list[i-1][j-1])), int(bool(sequence_list[i-1][j])))# Row 1
#                 adjacent_positions.append(int(bool(sequence_list[i][j-1])))# Row 2  
#             elif (i == MAX_I) & (j == 0): 
#                 adjacent_positions.append(int(bool(sequence_list[i-1][j])), int(bool(sequence_list[i-1][j+1])))# Row 1
#                 adjacent_positions.append( int(bool(sequence_list[i][j+1])))# Row 2  
#             # Check if less than 4
#             if sum(adjacent_positions) < 4: 
#                 NUMBER_OF_PAPER_ROLLS += 1

# print(NUMBER_OF_PAPER_ROLLS)
# NUMBER_OF_PAPER_ROLLS = 0

# for i in range(MAX_I):
#     for j in range(MAX_J):
#         if sequence_list[i][j] == '@': 
#             adjacent_positions = []
#             # Check adjacent positions
#             if (i > 0) & (j > 0) & (j < MAX_J) & (i < MAX_I): # No edge cases
#                 # print(i, j, MAX_J, MAX_I)
#                 adjacent_positions.extend([int(bool(sequence_list[i-1][j-1])), int(bool(sequence_list[i-1][j])), int(bool(sequence_list[i-1][j+1]))])# Row 1
#                 adjacent_positions.extend([int(bool(sequence_list[i][j-1])), int(bool(sequence_list[i][j+1]))])# Row 2 
#                 adjacent_positions.extend([int(bool(sequence_list[i+1][j-1])), int(bool(sequence_list[i+1][j])), int(bool(sequence_list[i+1][j+1]))])# Row 3
#             elif (i == 0) & (j > 0) & (j < MAX_J): 
#                 adjacent_positions.extend([int(bool(sequence_list[i][j-1])), int(bool(sequence_list[i][j+1]))])# Row 2 
#                 adjacent_positions.extend([int(bool(sequence_list[i+1][j-1])), int(bool(sequence_list[i+1][j])), int(bool(sequence_list[i+1][j+1]))])# Row 3 
#             elif (i == 0) & (j == MAX_J):
#                 adjacent_positions.extend([int(bool(sequence_list[i][j-1]))])# Row 2 
#                 adjacent_positions.extend([int(bool(sequence_list[i+1][j-1])), int(bool(sequence_list[i+1][j]))])# Row 3
#             elif (i == 0) & (j == 0):
#                 adjacent_positions.extend([int(bool(sequence_list[i][j+1]))])# Row 2 
#                 adjacent_positions.extend([int(bool(sequence_list[i+1][j])), int(bool(sequence_list[i+1][j+1]))])# Row 3 
#             elif (i == MAX_I) & (j > 0) & (j < MAX_J): 
#                 adjacent_positions.extend([int(bool(sequence_list[i-1][j-1])), int(bool(sequence_list[i-1][j])), int(bool(sequence_list[i-1][j+1]))])# Row 1
#                 adjacent_positions.extend([int(bool(sequence_list[i][j-1])), int(bool(sequence_list[i][j+1]))])# Row 2  
#             elif (i == MAX_I) & (j == MAX_J): 
#                 adjacent_positions.extend([int(bool(sequence_list[i-1][j-1])), int(bool(sequence_list[i-1][j]))])# Row 1
#                 adjacent_positions.extend([int(bool(sequence_list[i][j-1]))])# Row 2  
#             elif (i == MAX_I) & (j == 0): 
#                 adjacent_positions.extend([int(bool(sequence_list[i-1][j])), int(bool(sequence_list[i-1][j+1]))])# Row 1
#                 adjacent_positions.extend([int(bool(sequence_list[i][j+1]))])# Row 2  
#             # Check if less than 4
#             if sum(adjacent_positions) < 4: 
#                 NUMBER_OF_PAPER_ROLLS += 1

# print(NUMBER_OF_PAPER_ROLLS)


for i in range(MAX_I):
    for j in range(MAX_J):
        # print(i, j, sequence_list[i][j])
        if sequence_list[i][j] == '@': 
            # Chech surroundings 
            surrounding_symbol_count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]: 
                    if di == 0 and dj == 0: # Skip center
                        continue 
                    new_pos_i, new_pos_j = i + di, j + dj
                    if 0 <= new_pos_i < MAX_I and 0 <= new_pos_j < MAX_J: # check within bounds
                        if sequence_list[new_pos_i][new_pos_j] == '@':
                            surrounding_symbol_count += 1
            if surrounding_symbol_count < 4:
                NUMBER_OF_PAPER_ROLLS += 1 

print(NUMBER_OF_PAPER_ROLLS)