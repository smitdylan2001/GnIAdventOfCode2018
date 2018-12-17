def solve(input):
    with open(input) as f:
        for line in f:
            l = line
            break

    i = len(l) - 1
    while i > 0:
        lhs = ord(l[i])
        rhs = ord(l[i - 1])
        if abs(lhs - rhs) == 32:
            l = l[:i - 1] + l[i + 1:]
            i = len(l)
        i -= 1

    print(len(l))

solve("../input.txt")