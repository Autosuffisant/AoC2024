import re

with open('./input.txt') as f:
    data = f.read()

mul = re.compile(r'mul\((\d+),(\d+)\)')

data = mul.findall(data)

result = sum([int(i[0]) * int(i[1]) for i in data])

print(result)