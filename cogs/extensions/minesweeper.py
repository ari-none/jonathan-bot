import math
import random as r

# Cell adjacent indexes (for iterating)
adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Emoticon index for the symbols
image = {
    "#": "||<:t_e:1466133364103974973>||",
    "~": "<:t_e:1466133364103974973>",
    "@": "||<:t_b:1466133361914286160>||",
    "1": "||<:t_1:1466133352045351108>||",
    "2": "||<:t_2:1466133353441923375>||",
    "3": "||<:t_3:1466133354544893982>||",
    "4": "||<:t_4:1466133355736334357>||",
    "5": "||<:t_5:1466133356885573725>||",
    "6": "||<:t_6:1466133358164578395>||",
    "7": "||<:t_7:1466133359175663789>||",
    "8": "||<:t_8:1466133360643543051>||",
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

    mines = max(1, math.floor(math.sqrt(x * y))) * 2
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
                if minecount > 0:
                    grid[row][col] = str(minecount)

    x = len(grid)
    y = len(grid[0])
    freeslot = max(1, math.floor(math.sqrt(x * y)))
    placed = 0
    maxTries = 200

    while placed < freeslot:
        row = r.randint(0, x - 1)
        col = r.randint(0, y - 1)
        if grid[row][col] == "#":
            grid[row][col] = "~"  # Ats represents mines
            placed += 1
        maxTries -= 1
        if maxTries <= 0:
            break
    return grid

def randomgame(rows: int, cols: int) -> str:
    ret = ""
    grid, mines = minesgrid(rows, cols)
    grid = numfill(grid)

    ret += f"**{mines} mines on the field. Play by unspoilering the cells. If you hit a bomb, you lose. If you reveal all non-bomb tiles, you win !**\n\n"
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ret += image[grid[i][j]]
        ret += "\n"
    return ret