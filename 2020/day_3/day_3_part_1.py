import os
import sys

# Read data

with open(os.path.join(sys.path[0], 'input.txt'), 'r') as f:
    input_data = f.read().splitlines()

# Variables

first_line = True
pos_right = 0
sum_right = 3
length = 31
trees = 0

# Logic

for line in input_data:
    pos_right = pos_right % length
    if first_line:
        first_line = False
    else:
        line_print = list(line)
        if line[pos_right] == '#':
            trees += 1
    pos_right += sum_right

print(trees)
