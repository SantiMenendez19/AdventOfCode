import os
import re
import sys

# Read data

with open(os.path.join(sys.path[0], 'input.txt'), 'r') as f:
    input_data = f.read().splitlines()

valid_passports = 0
total_passports = 0

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
fields_encounted = fields.copy()

for line in input_data:
    print(line)
    if line == "":
        total_passports += 1
        if len(fields_encounted) == 0:
            valid_passports += 1
        fields_encounted = fields.copy()
    else:
        line = line.split(' ')
        for field in line:
            field = re.search(r'(\w+)(:)(.+)$', field).group(1)
            if field in fields_encounted:
                fields_encounted.remove(field)

# Last passport
total_passports += 1
if len(fields_encounted) == 0:
    valid_passports += 1

print(valid_passports)
print(total_passports)
