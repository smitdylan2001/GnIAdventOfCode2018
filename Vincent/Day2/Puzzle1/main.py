def solve(input):
    two = 0
    three = 0

    with open(input) as f:
        for line in f:
            d = {}
            for c in line:
                if not c in d:
                    d[c] = 1
                else:
                    d[c] += 1

            if 2 in d.values():
                two += 1
            if 3 in d.values():
                three += 1

    print(two * three)

solve("../input.txt")