with open('./input.txt') as f:
    data = f.read()

grid = [list(line) for line in data.splitlines()]

word = "XMAS"

directions = [
    (0, 1),   # Horizontal right
    (0, -1),  # Horizontal left
    (1, 0),   # Vertical down
    (-1, 0),  # Vertical up
    (1, 1),   # Diagonal down-right
    (-1, -1), # Diagonal up-left
    (1, -1),  # Diagonal down-left
    (-1, 1)   # Diagonal up-right
]

def countWord(grid, word, startRow, startCol, direction):
    rows, cols = len(grid), len(grid[0])
    wordLength = len(word)
    row, col = startRow, startCol
    vertical, horizontal = direction

    for i in range(wordLength):
        if not (0 <= row < rows and 0 <= col < cols):
            return 0
        if grid[row][col] != word[i]:
            return 0
        row += vertical
        col += horizontal

    return 1

def countAllOccurrences(grid, word):
    totalCount = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for direction in directions:
                totalCount += countWord(grid, word, row, col, direction)
    return totalCount

totalOccurrences = countAllOccurrences(grid, word)

print(totalOccurrences)
