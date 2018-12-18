__author__ = 'aoostdijk'

import operator

serial = 8141
w = 300
h = 300

# calculate the value of a cell
def calcValue(x,y):
    global serial

    rackID = x + 10
    plvl = rackID * y
    valueStr = str(( plvl + serial ) * rackID)
    return int(valueStr[-3]) - 5

# create dictionary with values
fcells = {}
for x in range(0,w+1):
    for y in range(0,h+1):
        # add in the 0's to prevent keyErrors
        #  when creating the summed area (see below)
        if x == 0 or y == 0:
            fcells[(x,y)] = 0
        else:
            fcells[(x,y)] = calcValue(x,y)

# Once I had a working example that would take at least an hour to compete
#  I started looking for some hints on how to improve the speed
#   (I'd tried every kind of list/dict selection in python)
#    and I learned about a "summed area" table, which is really neat!
#
# Basically, you sum the areas topleft of each cell, so that you can
#  very quickly calculate any sized area on the whole map
#  through: botRight - topRight - botLeft + topLeft
for x in range(1,w+1):
    for y in range(1,h+1):
        sums = fcells[(x,y)]
        sums += fcells[(x-1,y)]
        sums += fcells[(x,y-1)]
        sums -= fcells[(x-1,y-1)]
        fcells[(x,y)] = sums

# ready to parse!
result = None
highest = 0
for s in range(1,300):
    print(s)
    for x in range(1,w+1-s):
        for y in range(1,h+1-s):
            # too slow...
            # results[(x,y,s)] = sum([ sum(x) for x in [row[y-1:y-1+s] for row in fcells[x-1:x-1+s]] ])
            # print(x,y,s)

            # Here is that botRight - topRight - botLeft + topLeft
            val = fcells[(x+s,y+s)] - fcells[(x+s,y)] - fcells[(x,y+s)] + fcells[(x,y)]
            if val > highest:
                # through some error of mine these locations are offset by 1
                print(x+1,y+1,s,val)
                result = (x+1,y+1,s)
                highest = val

print(result)
print(highest)
