f = open('input12.txt')
lines = f.readlines()

numGens = 50000000000
offset = 100
initial = ".." * offset + lines[0][15:-1] + ".." * offset

patterns = {}
for i in range(2,len(lines)):
    # print(lines[i])
    patterns[lines[i][:5]] = lines[i][9]

def runGeneration(seq):
    new = seq
    for i in range(2,len(seq)-2):
        part = seq[i-2:i+3]
        if part in patterns.keys():
            new = new[:i] + patterns[part] + new[i+1:]
    return new

gen = 0
seq = initial
seen = {}
repeatStart = 0
repeatEnd = 0
fastforwarded = False
while gen < numGens:
    print(gen, seq)
    seq = runGeneration(seq)
    gen += 1

    # found a convergence of the shape at generation 113... extrapolate from there
    #  from gen 113 it steps to the right in its entirety by one pot
    if gen == 113:
        print(gen, seq)
        # all values will be offset by remaining generations
        remaining = numGens - gen
        pots = [i - ( offset * 2 ) + remaining for i in range(0, len(seq)) if seq[i] == "#"]
        print(sum(pots))
        break
