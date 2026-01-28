import math
import random as r

# Cell adjacent indexes (for iterating)
adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Emoticon index for the symbols
image = {
    "#": ""
}



# Actual code
def minesgrid(x: int=1, y: int=1) -> tuple[list[list[str]], int]:
    x = max(x, 1)
    y = max(y, 1)
    R = []
    for i in range(x):
        l = []
        for j in range(y):
            l.append("#") # Hashtags represents empty/safe tiles
        R.append(l)

    mines = max(1, math.floor(math.sqrt(x * y)))
    placed = 0

    while placed < mines:
        row = r.randint(0, x - 1)
        col = r.randint(0, y - 1)
        if R[row][col] != "@":
            R[row][col] = "@"  # Ats represents mines
            placed += 1

    return R, mines

def numcount(grid: list[list[str]], row: int, col: int) -> int:
    count = 0
    rows, cols = len(grid), len(grid[0])

    for ix, iy in adj: # For index X, index Y in adjacent list
        cx = row + ix # Check X
        cy = col + iy # Check Y
        if 0 <= cx < rows and 0 <= cy < cols:
            if grid[cx][cy] == "@":
                count += 1

    return count

def numfill(grid: list[list[str]]) -> list[list[str]]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != "@":
                minecount = numcount(grid, row, col)
                if minecount >= 0:
                    grid[row][col] = str(minecount)
    return grid

def randomgame(rows: int, cols: int) -> str:
    r = ""
    grid, mines = minesgrid(rows, cols)
    grid = numfill(grid)

    r += f":bomb: Number of mines : "
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            r += grid[i][j]
        r += "\n"
    return r