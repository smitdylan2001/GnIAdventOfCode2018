import re

def solve(input):
    grid = [[0 for i in range(1000)] for j in range(1000)]

    with open(input) as f:
        for line in f:
            matches = re.findall(r'[0-9]+', line)
            id = int(matches[0])
            x = int(matches[1])
            y = int(matches[2])
            w = int(matches[3])
            h = int(matches[4])

            for xPos in range(w):
                for yPos in range(h):
                    grid[x + xPos][y + yPos] += 1

    count = 0
    for xPos in range(len(grid)):
        for yPos in range(len(grid[xPos])):
            if grid[xPos][yPos] > 1:
                count += 1

    print(count)

solve("../input.txt")