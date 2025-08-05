#Assignment 11

import re

with open('assignment11.txt', 'r') as file:
    data = file.read()

numbers = re.findall('[0-9]+', data)
numbers = list(map(int, numbers))

total_sum = sum(numbers)
print(total_sum)