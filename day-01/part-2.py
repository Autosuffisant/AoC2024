with open('./input.txt') as f:
    data = f.read().splitlines()

col1 = []
col2 = dict()

for i in range(len(data)):
    line = data[i].split('   ')

    col1.append(int(line[0]))

    col2[int(line[1])] = col2.get(int(line[1]), 0) + int(line[1])

similarity = 0

for i in range(len(col1)):
    similarity += col2.get(col1[i], 0)

print(similarity)