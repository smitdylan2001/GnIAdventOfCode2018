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

    with open(input) as f:
        for line in f:
            matches = re.findall(r'[0-9]+', line)
            id = int(matches[0])
            x = int(matches[1])
            y = int(matches[2])
            w = int(matches[3])
            h = int(matches[4])

            found = True
            for xPos in range(w):
                for yPos in range(h):
                    if grid[x + xPos][y + yPos] > 1:
                        found = False
                        break
                if not found:
                    break

            if found:
                print(id)
                return

solve("../input.txt")