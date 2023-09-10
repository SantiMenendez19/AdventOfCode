import os
import sys

with open(os.path.join(sys.path[0], "input_day_1.txt"), "r") as f:
    input_data = f.read().splitlines()

# Get elf with carry most calories

elfs = []

calories = 0

for row in input_data:
    if row == "":
        elfs.append(calories)
        calories = 0
        continue

    calories += int(row.strip())

if calories > 0:
    elfs.append(calories)

print("Elf with most calories:", max(elfs))

# Find top 3 elfs with most calories

elfs.sort(reverse=True)

print("Top 3 elfs with most calories:", elfs[:3])
print("Sum: ", sum(elfs[:3]))
