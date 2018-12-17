import sys

def collapse(l):
    i = len(l) - 1
    while i > 0:
        lhs = ord(l[i])
        rhs = ord(l[i - 1])
        if abs(lhs - rhs) == 32:
            l = l[:i - 1] + l[i + 1:]
            i = min(i, len(l))
        i -= 1

    return len(l)

def solve(input):
    with open(input) as f:
        for line in f:
            inputLine = line
            break

    shortest = sys.maxsize
    for i in range(26):
        line = inputLine
        line = line.replace(chr(ord('A') + i), '')
        line = line.replace(chr(ord('a') + i), '')
        
        l = collapse(line)
        if l < shortest:
            shortest = l

    print(shortest)

solve("../input.txt")