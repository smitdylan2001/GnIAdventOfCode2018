# little class to store which ids claim which fabric index
class claim:
    def __init__(self):
        self.ids = []

    def count(self):
        return len(self.ids)

    def getIds(self):
        return self.ids

    def claim(self, id):
        self.ids.append(id)

# returns values from text line of claim (id, x, y, xs, ys)
def parseLine(line):
    line = line.replace(' ', '')
    s = line.split('@')
    id = int(s[0][1:])
    s = s[1].split(':')
    loc = s[0]
    x = int(loc.split(',')[0])
    y = int(loc.split(',')[1])
    size = s[1]
    xSize = int(size.split('x')[0])
    ySize = int(size.split('x')[1])

    return [ id, x, y, xSize, ySize ]

f = open('input3.txt')
lines = f.readlines()

# dict to store claim values per fabric index
data = {}
for i in range(1000*1000):
    data[i] = claim()

# dict to store claim data by claim id
raw = {}

# parse lines into data
for line in lines:
    parsed = parseLine(line)
    raw[parsed[0]] = parsed
    for x in range(parsed[1], parsed[1]+parsed[3]):
        for y in range(parsed[2], parsed[2]+parsed[4]):
            index = y * 1000 + x
            data[index].claim(parsed[0])

# count overlaps, and add any non-overlapping fabric index claim id's to search for non-overlaps
overlaps = 0
nonOverlapCandidates = set()
for i in data.values():
    if i.count() > 1:
        overlaps += 1
    if i.count() == 1:
        nonOverlapCandidates.add(i.getIds()[0])

print(overlaps)

# loop through all fabric indices of non-overlap candidates, only one should never invalidate (>1 claim)
for i in nonOverlapCandidates:
    raw_data = raw[i]
    invalidated = False
    for x in range(raw_data[1], raw_data[1]+raw_data[3]):
        for y in range(raw_data[2], raw_data[2]+raw_data[4]):
            index = y * 1000 + x
            if data[index].count() > 1:
                invalidated = True
    if not invalidated:
        print("Found non invalidated claim with id: "+str(raw_data[0]))