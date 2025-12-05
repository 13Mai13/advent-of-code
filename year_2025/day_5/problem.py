# Part 1

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence

data_path = Path(__file__).with_name("sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")

split_index = sequence_list.index('')
ranges_of_products = sequence_list[:split_index]
fresh_products = sequence_list[split_index + 1:]

# ALL_CANDIDATES = []

# for product_range in ranges_of_products:
#     start_end_range = product_range.split('-')
#     all_values = [x for x in range(int(start_end_range[0]), int(start_end_range[1]) + 1)]
#     ALL_CANDIDATES.extend(all_values)

# FRESH_PRODUCTS = 0

# for product in fresh_products:
#     if int(product) in set(ALL_CANDIDATES):
#         FRESH_PRODUCTS += 1
# print(FRESH_PRODUCTS)


# Parse ranges into (start, end) tuples
ranges = []
for product_range in ranges_of_products:
    start, end = product_range.split('-')
    ranges.append((int(start), int(end)))

# Check each product against all ranges
FRESH_PRODUCTS = 0
for product in fresh_products:
    product_id = int(product)
    # Check if product_id falls in ANY range
    for start, end in ranges:
        if start <= product_id <= end:
            FRESH_PRODUCTS += 1
            break  # Found it, no need to check other ranges

print(FRESH_PRODUCTS)