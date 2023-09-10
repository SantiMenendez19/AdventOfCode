import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    input_data = f.read().splitlines()

input_data = [int(x) for x in input_data]

for i in range(0, len(input_data)):
    for j in range(1 + i, len(input_data)):
        if i != j:
            if input_data[i] + input_data[j] == 2020:
                print(input_data[i], input_data[j])
                print(input_data[i] * input_data[j])
                break
