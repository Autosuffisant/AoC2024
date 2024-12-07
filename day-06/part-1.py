with open('./input.txt') as f:
    patrolMap = [list(line.strip()) for line in f]

    directions = [
        ("^", (-1, 0)),
        (">", (0, 1)),
        ("v", (1, 0)),
        ("<", (0, -1))
    ]

def getGuardPosition():
    for i in range(len(patrolMap)):
        for j in range(len(patrolMap[i])):
            if patrolMap[i][j] in [">", "<", "^", "v"]:
                return i, j

def getDirection(guardPosition):
    for direction in directions:
        if patrolMap[guardPosition[0]][guardPosition[1]] == direction[0]:
            return direction

steps = 1
rows, cols = len(patrolMap), len(patrolMap);
guardX, guardY = getGuardPosition()
guardDirection = getDirection((guardX, guardY))

nextX, nextY = guardX + guardDirection[1][0], guardY + guardDirection[1][1]


while 0 <= nextX < rows and 0 <= nextY < cols:
    if patrolMap[nextX][nextY] == "#":
        directionIndex = directions.index(guardDirection) + 1
        if directionIndex > 3:
            directionIndex = 0

        guardDirection = directions[directionIndex]
    else:
        if (patrolMap[guardX][guardY] != "X"):
            patrolMap[guardX][guardY] = "X"
            steps += 1
        guardX, guardY = nextX, nextY
    nextX, nextY = guardX + guardDirection[1][0], guardY + guardDirection[1][1]


print(steps)