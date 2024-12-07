with open('./input.txt') as f:
    patrolMap = [list(line.strip()) for line in f]

directions = [
    ("^", (-1, 0)),
    (">", (0, 1)),
    ("v", (1, 0)),
    ("<", (0, -1))
]

for r, row in enumerate(patrolMap):
    for c, cell in enumerate(row):
        if cell in "^>v<":
            guardStart = (r, c)
            guardStartDirection = cell

directionsDirectionnary = {d[0]: d[1] for d in directions}

def simulatePatrol(grid, obstruction=None):
    rows, cols = len(grid), len(grid[0])
    guardPosition = guardStart
    guardDirection = guardStartDirection
    visited = set()
    history = set()

    while True:
        state = (guardPosition[0], guardPosition[1], guardDirection)
        if state in history:
            return True
        history.add(state)

        currentDirection = directionsDirectionnary[guardDirection]
        nextPosition = (guardPosition[0] + currentDirection[0], guardPosition[1] + currentDirection[1])

        if not (0 <= nextPosition[0] < rows and 0 <= nextPosition[1] < cols):
            return False

        if obstruction == nextPosition or grid[nextPosition[0]][nextPosition[1]] == "#":
            guardDirection = directions[(directions.index((guardDirection, currentDirection)) + 1) % 4][0]
        else:
            guardPosition = nextPosition
            visited.add(guardPosition)

rows, cols = len(patrolMap), len(patrolMap[0])
validObstructions = 0

for r in range(rows):
    for c in range(cols):
        if (r, c) == guardStart or patrolMap[r][c] == "#":
            continue

        if simulatePatrol(patrolMap, obstruction=(r, c)):
            validObstructions += 1

print(validObstructions)
