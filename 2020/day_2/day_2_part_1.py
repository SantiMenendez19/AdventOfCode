import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    input_data = f.read().splitlines()

valid_passwords = 0

for data in input_data:
    times, char, password = data.split(" ")
    min_times, max_times = times.split("-")
    min_times = int(min_times)
    max_times = int(max_times)
    char = char.split(":")[0]
    count_char = password.count(char)
    if min_times <= count_char <= max_times:
        valid_passwords += 1

print(valid_passwords)
