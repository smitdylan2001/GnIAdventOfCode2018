def solve(input):
    n = 0
    with open(input) as f:
        for line in f:
            n += int(line)

    print(n)

solve("../input.txt")