import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")

# Part 1

MAX_SUM = 0

for bank in sequence_list: 

    # This approach is wrong because position matters

    # max_1 = max(battery)
    # battery_no_first_max = battery.replace(max_1, '')
    # max_2 = max(battery_no_first_max)

    # print(battery, max_1, max_2)

    # MAX_SUM += int(max_1) + int(max_2)

    # LOCAL_MAX = (0, 0) # number, position
    # LOCAL_MAX_2 = (0, 0)

        # for position, number in enumerate(battery):

        # print(position, number, type(position), type(number))
        # print(int(number), LOCAL_MAX[0], type(int(number)), type(LOCAL_MAX[0]))

        # if int(number) > LOCAL_MAX[0]: 
        #     LOCAL_MAX_2 = LOCAL_MAX
        #     LOCAL_MAX = (int(number), position)
        # elif int(number) > LOCAL_MAX_2[0] &:
        #     LOCAL_MAX_2 = (int(number), position)

    # if LOCAL_MAX[1] < LOCAL_MAX_2[1]:
    #     biggest_number = int(str(LOCAL_MAX[0]) + str(LOCAL_MAX_2[0]))
    # else: 
    #     biggest_number = int(str(LOCAL_MAX_2[0]) + str(LOCAL_MAX[0]))
    # print(battery,LOCAL_MAX, LOCAL_MAX_2, biggest_number )
    # MAX_SUM += biggest_number

    max_joltage = 0
    
    # Check all consecutive pairs of digits
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form a two-digit number from batteries at positions i and j
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    MAX_SUM +=max_joltage 

print(MAX_SUM)
MAX_SUM = 0

# Part 2

for bank in sequence_list: 

    max_joltage = 0
    
    result = []
    start = 0
    
    for i in range(12):
        # We need to select (n - i) more digits total
        # We can search up to position where we still have enough digits left
        max_pos = len(bank) - (12 - i) + 1
        
        # Find the largest digit in the valid range
        max_digit = '0'
        max_idx = start
        
        for j in range(start, max_pos):
            if bank[j] > max_digit:
                max_digit = bank[j]
                max_idx = j
        
        result.append(max_digit)
        start = max_idx + 1
    
    max_joltage = int(''.join(result))
    MAX_SUM +=max_joltage 
print(MAX_SUM)