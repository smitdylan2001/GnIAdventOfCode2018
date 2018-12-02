def findSimilarLines(lines):
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            count = 0
            for k in range(len(lines[i])):
                if lines[i][k] != lines[j][k]:
                    count += 1
                    if count > 1:
                        break
            
            if count == 1:
                return (lines[i], lines[j])

def solve(input):
    lines = []

    with open(input) as f:
        for line in f:
            lines.append(line)

    similarLines = findSimilarLines(lines)

    common = ""
    for i in range(len(similarLines[0])):
        if similarLines[0][i] == similarLines[1][i]:
            common += similarLines[0][i]

    print(common)

solve("../input.txt")