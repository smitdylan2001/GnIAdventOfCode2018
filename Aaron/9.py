__author__ = 'aoostdijk'

playerCount = 403
lastMarble = 71920 * 100 # * 100 takes under 30 seconds...

# Quick test with known result
# playerCount = 10
# lastMarble = 1618

# player score dict
playerScore = {}
for n in range(playerCount):
    playerScore[n] = 0

# double linked list, much faster than lists
#  and ideal because we don't care about the size
#   and are always working from a "current node"
class dllist:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

# the first insert of the list is the 0 marble
marbles = dllist(0)

# if we let the linked list loop back on itself
#  this particular challenge becomes a lot simpler
marbles.next = marbles.prev = marbles

# start at root
current = marbles
marbleNum = 1
playerIndex = 0

# run as many times as needed until we reach target marble
while marbleNum <= lastMarble:
    if marbleNum % 23 == 0:
        # 7 steps back, and since it loops, that's easy!
        # for i in range(7):
        #    current = current.prev
        # I wondered if this was faster at all...
        current = current.prev.prev.prev.prev.prev.prev.prev

        # update score
        playerScore[playerIndex % playerCount] += current.value + marbleNum

        # pop this instance from the list
        current.prev.next = current.next
        current.next.prev = current.prev
        current = current.next
    else:
        # step to next
        current = current.next

        # make new list instance for marble
        new = dllist(marbleNum)

        # insert right of current, and connect all the other points
        new.next = current.next
        new.prev = current
        current.next.prev = new
        current.next = new

        # finally step to new insert
        current = new

    playerIndex += 1
    marbleNum += 1

    # Debug array for first x runs to check with example insertion logic
    # start = marbles
    # toPrint = str(start.value)
    # cur = start.next
    # while cur.value != start.value:
    #     toPrint += "," + str(cur.value)
    #    cur = cur.next
    # print(toPrint)
    #
    # if marbleNum > 25: break

print(sorted(playerScore.values(), reverse=True))