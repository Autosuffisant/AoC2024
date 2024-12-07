with open('./input.txt') as f:
    data = f.read().splitlines()

col1 = []
col2 = []

for i in range(len(data)):
    line = data[i].split('   ')

    col1.append(int(line[0]))
    col2.append(int(line[1]))

col1.sort()
col2.sort()

distances = sum([abs(int(col1[i]) - int(col2[i])) for i in range(len(col1))])

print(distances)