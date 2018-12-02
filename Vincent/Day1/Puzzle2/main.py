def solve(input):
    n = 0
    d = { 0: 1 }
    found = False

    while not found:
        with open(input) as f:
            for line in f:
                n += int(line)
                if not n in d:
                    d[n] = 1
                else:
                    found = True
                    break

    print(n)

solve("../input.txt")