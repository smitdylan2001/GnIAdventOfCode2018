class Point:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

class Area:
    def __init__(self, pointId, coords):
        self.pointId = pointId
        # look, I used something I've never used before!
        # this gets all points from coords that match our pointId as their value (closest)
        self.points = {key: value for key, value in coords.items() if value == pointId}
        self.infinite = False

        # area is infinite if it contains points on the borders
        # top
        for i in range(400):
            if i in self.points.keys():
                self.infinite = True
        # bottom
        for i in range(400*399, 400*400):
            if i in self.points.keys():
                self.infinite = True
        # left
        for i in range(0,400*400, 400):
            if i in self.points.keys():
                self.infinite = True
        # right
        for i in range(399,400*400, 400):
            if i in self.points.keys():
                self.infinite = True

        # brute force
        # for x in range(400):
        #     for y in range(400):
        #         if x == 0 or y == 0 or x == 399 or y == 399:
        #             if (y + x * 400) in self.points.keys():
        #                 self.infinite = True

    def length(self):
        return len(self.points)

def manhattenDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# read lines
f = open('input6.txt')
lines = f.readlines()

# render into points
points = []

i = 0
for line in lines:
    line = line.replace(' ', '')
    p = line.split(',')
    points.append(Point(int(p[0]), int(p[1]), i))
    i += 1

# match coordinate indices to closest point index
coords = {}
for x in range(400):
    for y in range(400):
        closestD = 9999
        closestPoint = None
        for p in points:
            d = manhattenDistance(p.x, p.y, x, y)
            if d < closestD:
                closestPoint = p
                closestD = d
            elif d == closestD:
                closestPoint = None

        if closestPoint is None:
            coords[y + x * 400] = -1    # more than one closest point
        else:
            coords[y + x * 400] = closestPoint.id

# create areas from coord dictionary (they self-select their points)
areas = []
largest = 0
for i in range(len(points)):
    a = Area(i, coords)
    areas.append(a)
    # get largest area that isn't infinite
    if not a.infinite and a.length() > largest:
        largest = a.length()

# puzzle 1
print(largest)

# re-loop all coordinates and count sum to all points
#  I'm pretty sure there's a lamba-like way to do this differently
#   but it might not be faster
pointCount = 0
for x in range(400):
    for y in range(400):
        sum = 0
        for p in points:
            sum += manhattenDistance(p.x, p.y, x, y)
        if sum < 10000:
            pointCount += 1

# puzzle 2
print(pointCount)
