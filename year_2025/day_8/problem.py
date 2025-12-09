# Part 1
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2]))
from year_2025.utils import read_sequence
from math import sqrt

data_path = Path(__file__).with_name("sequence.txt")
sequence_list = read_sequence(str(data_path), delimiter="\n")

# Parse coordinates as integers
points = []
for seq in sequence_list:
    x, y, z = seq.split(',')
    points.append((int(x), int(y), int(z)))

print(f"Total points: {len(points)}")

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

# Calculate all pairwise distances
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = distance(points[i], points[j])
        distances.append((dist, i, j))

print(f"Total pairs: {len(distances)}")

# Sort by distance (shortest first)
distances.sort()

# Union-Find data structure to track circuits
parent = list(range(len(points)))
size = [1] * len(points)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x == root_y:
        return False
    
    if size[root_x] < size[root_y]:
        parent[root_x] = root_y
        size[root_y] += size[root_x]
    else:
        parent[root_y] = root_x
        size[root_x] += size[root_y]
    
    return True

# Process the 1000 shortest pairs (attempt to connect them)
connections_attempted = 0
connections_successful = 0

for dist, i, j in distances:
    union(i, j)  # Attempt connection (might fail if already connected)
    connections_attempted += 1
    
    if connections_attempted == 1000:
        break

print(f"Connections attempted: {connections_attempted}")

# Find all circuit sizes
circuit_sizes = []
for i in range(len(points)):
    if find(i) == i:
        circuit_sizes.append(size[i])

circuit_sizes.sort(reverse=True)

print(f"Number of circuits: {len(circuit_sizes)}")
print(f"Circuit sizes: {circuit_sizes}")

# Check if we have at least 3 circuits
if len(circuit_sizes) >= 3:
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    print(f"Three largest circuits: {circuit_sizes[:3]}")
    print(f"Result: {result}")
else:
    print(f"Only {len(circuit_sizes)} circuit(s) found!")