__author__ = 'aoostdijk'

# stores references to child nodes and stores meta
#  need to parse the tree into this first before we can calculate value
#   because it relies on the metadata (which is after child nodes)
class Node:
    def __init__(self):
        self.children = []
        self.meta = []
        pass

    def addChild(self, child):
        self.children.append(child)

    def setMeta(self, meta):
        self.meta = meta

    def getValue(self):
        if len(self.children) == 0:
            return sum(self.meta)
        else:
            value = 0
            validIndices = [x for x in self.meta if x <= len(self.children)]
            for i in validIndices:
                if i == 0: continue
                value += self.children[i-1].getValue()
            return value

f = open('input8.txt')

# read file, split into array, convert to ints
s = f.read()
s = s.split(' ')
s = [int(x) for x in s]

metaCount = 0

# recursive function that returns updated index and parsed node
def readNodes(data, index):
    global metaCount
    node = Node()

    # get children and meta counts
    childs = data[index]
    index += 1
    metaData = data[index]
    index += 1

    # read children
    while childs > 0:
        ret = readNodes(data, index)
        index = ret[0]
        node.addChild(ret[1])
        childs -= 1

    # read meta
    meta = []
    while metaData > 0:
        metaCount += data[index]
        meta.append(data[index])
        index += 1
        metaData -= 1

    node.setMeta(meta)

    return index, node

# parse tree from beginning
ret = readNodes(s, 0)
print(metaCount)
print(ret[1].getValue())
