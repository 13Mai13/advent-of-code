from pathlib import Path

try:
    from year_2025.utils import read_sequence
except ModuleNotFoundError:
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[2]))
    from year_2025.utils import read_sequence


# Constants
STARTING_POINT = 50
NUMBER_OF_TIMES_DIAL_POINTED_TO_0= 0

data_path = Path(__file__).with_name("sequence.txt")
sequence_list = read_sequence(str(data_path))

# Part 1

current_position = STARTING_POINT

for instruction in sequence_list:

    try:
        steps = int(instruction[1:])
        if instruction[0] == "R":
            current_position = (current_position + steps) % 100
        elif instruction[0] == "L":
            current_position = (current_position - steps) % 100
        # Wrong because it shoul be > 100
        # if "R" in instruction:
        #     if current_position + steps > 99:
        #         current_position = current_position + steps - 100
        #     else:
        #         current_position = current_position + steps
        # if "L" in instruction:
        #     if current_position - steps < 0:
        #         current_position = current_position - steps + 100
        #     else:
        #         current_position = current_position - steps
        if current_position == 0:
            NUMBER_OF_TIMES_DIAL_POINTED_TO_0 += 1

    except ValueError:
        raise ValueError(f"Invalid instruction: {instruction}")

print(NUMBER_OF_TIMES_DIAL_POINTED_TO_0)

# Part 2 
NUMBER_OF_TIMES_DIAL_POINTED_TO_0 = 0
current_position = STARTING_POINT
for instruction in sequence_list:
    steps = int(instruction[1:])
    if instruction[0] == "R":
        for _ in range(steps):
            current_position = (current_position + 1) % 100
            if current_position == 0:
                NUMBER_OF_TIMES_DIAL_POINTED_TO_0 += 1
                
    elif instruction[0] == "L":
        for _ in range(steps):
            current_position = (current_position - 1) % 100
            if current_position == 0:
                NUMBER_OF_TIMES_DIAL_POINTED_TO_0 += 1

print(NUMBER_OF_TIMES_DIAL_POINTED_TO_0)
    