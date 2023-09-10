import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    input_data = f.read().splitlines()

valid_passwords = 0

for data in input_data:
    positions, char, password = data.split(" ")
    pos_1, pos_2 = positions.split("-")
    pos_1 = int(pos_1)
    pos_2 = int(pos_2)
    char = char.split(":")[0]
    if password[pos_1 - 1] == char and not password[pos_2 - 1] == char:
        valid_passwords += 1
    elif password[pos_2 - 1] == char and not password[pos_1 - 1] == char:
        valid_passwords += 1
    else:
        continue

print(valid_passwords)
