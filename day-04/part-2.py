# Read input
with open('./input.txt') as f:
    data = f.read()

grid = [list(line) for line in data.splitlines()]

words = ["SAM", "MAS"]
diagonalDirections = [
    ((-1, -1), (0, 0), (1, 1)),  # Top-left to bottom-right
    ((-1, 1), (0, 0), (1, -1))   # Top-right to bottom-left
]

def checkXmas(grid, center_row, center_col):
    for diagonal in diagonalDirections:
        word = []
        for (rowDelta, colDelta) in diagonal:
            word.append(grid[center_row + rowDelta][center_col + colDelta])
        if "".join(word) not in words:
            return False
    return True

def countXmas(grid):
    totalCount = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == "A":  # The center of the "X-MAS" must be "A"
                if checkXmas(grid, row, col):
                    totalCount += 1
    return totalCount

total_occurrences = countXmas(grid)

print(f"Total occurrences of 'X-MAS': {total_occurrences}")
