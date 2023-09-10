import os
import sys

# Read data
map_trees = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as f:
    input_data = f.read().splitlines()
for line in input_data:
    map_trees.append(list(line))

# Variables
length_row = 31
length_col = len(map_trees)
mult_trees = 1


# Logic

for sum_right, sum_down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    pos_right = 0
    pos_down = 0
    trees = 0
    while pos_down < length_col - 1:
        pos_right += sum_right
        pos_right = pos_right % length_row
        pos_down += sum_down
        if map_trees[pos_down][pos_right] == '#':
            trees += 1
    print(trees)
    mult_trees *= trees

print(mult_trees)
