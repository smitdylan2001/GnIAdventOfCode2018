import operator
import os

WALL = 0
ELF = 1
GOBLIN = 2
SPACE = 3

conversion = {WALL: "#", ELF: "E", GOBLIN: "G", SPACE: "."}

class Unit:
    def __init__(self, x, y, type, powerOffset):
        self.x = x
        self.y = y
        self.type = type
        self.power = 3 + powerOffset
        self.hp = 200
        self.following = False

    def distanceTo(self, node):
        return abs(node.x - self.x) + abs(node.y - self.y)

    def moveTowards(self, node):
        global field

        moveNodes = field[(self.x,self.y)].adjacent()
        paths = []
        for i in moveNodes:
            if self.following:
                print(i)
            path = self.shortestPathTo(i, node, False)
            if path is not None and len(path) > 0:
                paths.append(path)

        if self.following:
            print(self.x, self.y, len(paths))
            for p in paths:
                print(p)

        if len(paths) > 0:
            # which path is the shortest length
            paths.sort(key=len)
            shortest = len(paths[0])
            paths = [p for p in paths if len(p) == shortest]

            # get every first step of all paths of equal shortness
            steps = [p[0] for p in paths]
            # sort them by reading order
            steps.sort(key=getIndex)
            # get first
            step = steps[0]

            # leave node I was at
            field[(self.x,self.y)].empty = True

            # occupy node I am moving towards
            field[step].empty = False
            self.x = step[0]
            self.y = step[1]
        else:
            print("Got none path!")

    def shortestPathTo(self, start, target, popFirst):
        debug = False # (self.x == 14 and self.y == 6 and target.x == 18 and target.y == 26)
        seen = set()
        new = [PathNode(start, None)]

        while len(new) > 0:
            # sort these based on f
            new.sort(key=operator.attrgetter('f'))
            current_node = new.pop(0)

            if current_node.position in seen:
                continue

            seen.add(current_node.position)

            # if debug:
            #    print("current", current_node.position)

            if current_node.position == (target.x,target.y):
                # found path, backtrace
                path = []
                current = current_node

                while current is not None:
                    # print("Found")
                    path.append(current.position)
                    current = current.parent

                path = path[::-1]
                if popFirst:
                    path.pop(0)
                return path

            children = []
            for pos in field[current_node.position].adjacent():
                new_node = PathNode(pos, current_node)
                children.append(new_node)

            found = False
            for child in children:
                if child.position in seen:
                    continue
                else:
                    # Create the f, g, and h values
                    child.g = current_node.g + 1
                    child.h = ((child.position[0] - target.x) ** 2) + ((child.position[1] - target.y) ** 2)
                    child.f = child.g + child.h

                    for n in new:
                        if n.position == child.position and child.g > n.g:
                            continue

                    new.append(child)

        return None

    def attack(self, unit):
        return unit.attacked(self)

    def attacked(self, attacker):
        global units
        global field
        self.hp -= attacker.power
        if self.hp <= 0:
            print(conversion[self.type], "died")
            field[(self.x,self.y)].empty = True
            return True
        return False

class PathNode:
    def __init__(self, position, parent):
        self.position = position
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0

class Node:
    def __init__(self, x, y, char, powerOffset):
        global units, following
        self.x = x
        self.y = y
        # space is default
        self.type = SPACE
        self.empty = True
        if char == "#":
            self.type = WALL
            self.empty = False
        elif char == "G":
            self.empty = False
            units.append(Unit(x,y,GOBLIN, 0))
            if not following:
                units[len(units)-1].following = True
                following = True
        elif char == "E":
            units.append(Unit(x, y, ELF, powerOffset))
            self.empty = False

    def adjacent(self):
        global field
        return [ n for n in [ (self.x,self.y+1), (self.x+1,self.y), (self.x-1,self.y), (self.x,self.y-1) ] if n in field.keys() and field[n].empty ]

def getIndex(pos):
    global width
    return pos[1] * width + pos[0]

def addIfEmptyAndReachable(unit, targetUnit, x, y, list):
    global field
    target = field[(targetUnit.x + x, targetUnit.y + y)]
    if target.empty:
        path = unit.shortestPathTo((unit.x,unit.y), target, True)
        if path is not None:
            list.append((target, len(path)))

def typeToStr(type):
    return conversion[type]

def renderMap():
    global field, units, width, height
    for y in range(width):
        line = ""
        for x in range(height):
            found = False
            for u in units:
                if u.x == x and u.y == y and u.hp > 0:
                    line += typeToStr(u.type)
                    found = True
                    break
            if not found:
                line += typeToStr(field[(x,y)].type)
        print(line)


f = open('input15.txt')
lines = f.readlines()

field = {}
units = []
width = len(lines[0])-1 # due to \n
height = len(lines)
following = True

def runIteration(count, step, direction):
    print("RUNNING", count, step, direction)
    global field, units
    field = {}
    units = []

    startNext = False

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            field[(x,y)] = Node(x, y, lines[y][x], count)

    combat = True
    round = 0
    while combat:
        units = [ u for u in units if u.hp > 0 ]
        units.sort(key=operator.attrgetter('y', 'x'))
        # print( [conversion[u.type] for u in units if u.hp > 0] )

        for unit in units:
            # skip turns for dead units
            if unit.hp <= 0:
                print("skipping dead unit")
                continue

            enemies = [ u for u in units if u.type != unit.type and u.hp > 0 ]
            enemies.sort(key=operator.attrgetter('y', 'x'))  # is this already the case?

            if len(enemies) == 0:
                combat = False
                total = 0
                for u in units:
                    if u.hp > 0:
                        print(conversion[u.type], u.hp)
                        total += u.hp
                print( "Combat finished: ", total, round, round * total )
                break

            inRange = [u for u in enemies if abs(u.x - unit.x) == 1 and u.y == unit.y or abs(u.y - unit.y) == 1 and u.x == unit.x and u.hp > 0]
            if len(inRange) != 0:
                inRange.sort(key=operator.attrgetter('hp'))
                lowest = inRange[0].hp
                inRange = [n for n in inRange if n.hp == lowest]
                inRange.sort(key=operator.attrgetter('y', 'x'))
                if inRange[0].hp <= 0:
                    print("WTD DUDE")
                if unit.attack(inRange[0]):
                    if unit.type == GOBLIN:
                        combat = False
                        startNext = True
                        break
            else:
                # print("getting available")
                availablePositions = []
                for e in enemies:
                    # print("1")
                    addIfEmptyAndReachable(unit, e, -1, 0, availablePositions)
                    # print("2", ( unit.x, unit.y ), ( e.x, e.y ))
                    addIfEmptyAndReachable(unit, e, 1, 0, availablePositions)
                    # print("3")
                    addIfEmptyAndReachable(unit, e, 0, -1, availablePositions)
                    # print("4")
                    addIfEmptyAndReachable(unit, e, 0, 1, availablePositions)

                if len(availablePositions) == 0:
                    continue

                # sort based on path length
                availablePositions.sort(key=operator.itemgetter(1))
                # print(availablePositions)
                shortest = availablePositions[0][1]
                # remove all non shortest paths
                availablePositions = [ n for n in availablePositions if n[1] == shortest ]
                # get nodes
                availablePositions = [ n[0] for n in availablePositions ]
                # sort top-left to bottom-right
                availablePositions.sort(key=operator.attrgetter('y', 'x'))
                # move towards selected
                unit.moveTowards(availablePositions[0])

                # try to attack again
                inRange = [u for u in enemies if abs(u.x - unit.x) == 1 and u.y == unit.y or abs(u.y - unit.y) == 1 and u.x == unit.x and u.hp > 0]
                if len(inRange) != 0:
                    inRange.sort(key=operator.attrgetter('hp'))
                    lowest = inRange[0].hp
                    inRange = [ n for n in inRange if n.hp == lowest ]
                    inRange.sort(key=operator.attrgetter('y', 'x'))
                    if unit.attack(inRange[0]):
                        if unit.type == GOBLIN:
                            combat = False
                            startNext = True
                            break

        round += 1
        print(round)
        renderMap()

    if startNext:
        if step == 1:
            # we just stepped back one and lost, stop!
            print("First loss at step 1:", count)
            return
        if direction == -1:
            step = int(step / 2)
        direction = 1
        runIteration(count + step * direction, step, direction)
    else:
        if step == 1:
            print("Successful win without ELF losses at power offset:", count)

        if direction == 1:
            step = max(1, int(step / 2))
        direction = -1
        runIteration(count + step * direction, step, direction)

runIteration(1, 50, 1)