import operator

class Node:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

        # self.left = None
        # self.right = None
        # self.up = None
        # self.down = None

        # if type == 0:   # straightaway
        #     pass
        # elif type == 1: # corner-clockwise
        #     pass
        # elif type == 2: # corner-counterclockwise
        #     pass
        # elif type == 3: # intersection
        #     pass

def debugRenderMapWithCarts():
    global lines
    size = len(lines[0])
    debug = []
    for ty in range(0, len(lines)):
        str = ""
        for tx in range(0, len(lines[ty])):
            found = False
            for cart in carts:
                if cart.x == tx and cart.y == ty:
                    str += cart.getSymbol()
                    found = True
            if not found:
                str += lines[ty][tx]
        debug.append( str.strip('\n') )

    for i in range(len(debug)):
        print(debug[i])
    print()

def debugRenderMap(x,y,size):
    global lines
    left = x - size
    top = y - size
    debug = []
    for ty in range(top, top + size * 2):
        debug.append( str(ty) + ": "+ lines[ty][left:left+size*2] )

    print(left,left+size*2)
    for i in range(len(debug)):
        if i == size or i == size+1:
            print()
        print(debug[i])

class Cart:
    def __init__(self, x, y, xdir, ydir, node ):
        self.x = x
        self.y = y
        self.xdir = xdir
        self.ydir = ydir
        self.steer = [-1, 0, 1]
        self.node = node
        self.steerStep = 0
        self.stepped = True

    def move(self, nodes):
        if self.stepped:
            return True

        self.stepped = True

        # handle directional behaviour of current node
        if self.node is None or self.node.type == 0:
            pass
        elif self.node.type == 1:
            if self.xdir == 0:
                self.turnRight()
            else:
                self.turnLeft()
        elif self.node.type == 2:
            if self.xdir == 0:
                self.turnLeft()
            else:
                self.turnRight()
            pass
        elif self.node.type == 3:
            act = self.steer[self.steerStep % 3]
            self.steerStep += 1
            if act == -1:
                self.turnLeft()
            elif act == 1:
                self.turnRight()

        return self.forward(nodes)

    def forward(self, nodes):
        self.x += self.xdir
        self.y += self.ydir
        try:
            self.node = nodes[(self.x, self.y)]
            return True
        except KeyError:
            print("Error at", self.x, self.y)
            debugRenderMap(self.x, self.y, 10)
            return False

    def turnRight(self):
        tx = self.xdir
        self.xdir = -self.ydir
        self.ydir = tx
        pass

    def turnLeft(self):
        tx = self.xdir
        self.xdir = self.ydir
        self.ydir = -tx
        pass

    def getSymbol(self):
        if self.xdir < 0:
            return "<"
        elif self.xdir > 0:
            return ">"
        elif self.ydir < 0:
            return "^"
        else:
            return "v"

nodes = {}
carts = []
f = open('input13.txt')
lines = f.readlines()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        node = None
        cart = None
        pos = lines[y][x]
        # nodes
        if pos == "-" or pos == "|":
            node = Node(x,y,0)
        elif pos == "/":
            node = Node(x,y,1)
        elif pos == "\\":
            node = Node(x, y, 2)
        elif pos == "+":
            node = Node(x, y, 3)
        # carts
        elif pos == ">":
            cart = Cart(x,y,1,0,None)
            node = Node(x, y, 0)
        elif pos == "<":
            cart = Cart(x,y,-1,0,None)
            node = Node(x, y, 0)
        elif pos == "^":
            cart = Cart(x,y,0,-1,None)
            node = Node(x, y, 0)
        elif pos == "v":
            cart = Cart(x,y,0,1,None)
            node = Node(x, y, 0)
        elif pos == " ":
            pass
        # else:
        #    print("found weird ass thing", ord(pos))

        # store for neighbor retrieval
        if node is not None:
            nodes[(x,y)] = node
        if cart is not None:
            carts.append(cart)

for i in range(len(lines)):
    lines[i] = lines[i].replace(">", "-")
    lines[i] = lines[i].replace("<", "-")
    lines[i] = lines[i].replace("v", "|")
    lines[i] = lines[i].replace("^", "|")

# for node in nodes.values():
#     if (node.x-1, node.y) in nodes.keys():
#         node.left = nodes[(node.x-1, node.y)]
#     if (node.x+1, node.y) in nodes.keys():
#         node.right = nodes[(node.x+1, node.y)]
#     if (node.x, node.y-1) in nodes.keys():
#         node.down = nodes[(node.x, node.y-1)]
#     if (node.x, node.y+1) in nodes.keys():
#         node.up = nodes[(node.x, node.y+1)]

def handleCollisions():
    global carts
    _collision = False
    _haveSeenCollision = False
    _i = 0

    # check if any carts are in the same spot
    _loop = len(carts)
    while _i < _loop:
        for j in range(_i + 1, _loop):
            if carts[_i].x == carts[j].x and carts[_i].y == carts[j].y:
                _collision = True
                _haveSeenCollision = True
                # print("Collision at step:", steps + 1, "for position: ", carts[_i].x, carts[_i].y, "between carts", _i, j)
                # debugRenderMap(carts[j].x, carts[j].y, 2)
                cart1 = carts[_i]
                cart2 = carts[j]
                carts.remove(cart1)
                carts.remove(cart2)
                # for cart in carts:
                #     print(cart.x, cart.y)
                break

        if _collision:
            _collision = False
            _i = -1
            _loop = len(carts)

        _i += 1
    return _haveSeenCollision

steps = 0
followCart = carts[0]

# sort carts by y,x position
carts.sort(key=operator.attrgetter('y', 'x'))

# debugRenderMapWithCarts()

while len(carts) > 0:
    stop = False

    carts.sort(key=operator.attrgetter('y', 'x'))

    for cart in carts:
        cart.stepped = False

    loop = len(carts)
    x = 0
    while x < loop:
        cart = carts[x]
        cart.move(nodes)
        if handleCollisions():
            x = -1
            loop = len(carts)
        x += 1

    # debugRenderMapWithCarts()

    if stop:
        print("ERROR", steps)
        break

    steps += 1

    if len(carts) == 1:
        print(carts[0].x, carts[0].y)
        break