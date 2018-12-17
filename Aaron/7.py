def parseLine(line):
    # instance, dependency
    return line[36], line[5]

# read lines
f = open('input7.txt')
lines = f.readlines()

# Build dependencies dictionary
dependencies = {}
for line in lines:
    parsed = parseLine(line)
    if parsed[0] not in dependencies.keys():
        dependencies[parsed[0]] = set()
    dependencies[parsed[0]].add(parsed[1])

# Add missing keys (no dependencies, so possible starters)
for i in range(97,97+26):
    k = str.upper(chr(i))
    if k not in dependencies.keys():
        dependencies[k] = set()

# get sorted keys
sortedKeys = sorted(dependencies)
active = set()
order = ""

# function to get next available (sorted) key
def getNextAvailable(running):
    for k in sortedKeys:
        # skip checks of already active elements
        if k in active or k in running.keys():
            continue

        # check if all our dependencies are active
        available = True
        for v in dependencies[k]:
            if v not in active:
                available = False

        if available:
            return k
    return None

# the above function makes this loop very simple
#  assuming there is always a next available (which we can)
while len(active) < len(sortedKeys):
    k = getNextAvailable({})
    order += k
    active.add(k)
    # print("Handled " + k)

# puzzle 1
print(order, len(order))
print()

# reset all our variables
runningTasks = {}
active = set()
totalTime = 0
WORKERS = 5
order = ""

# Does roughly the same thing, but pushes tasks onto a "running" dictionary
#  where they are assigned a time until completion that ticks down.
# Each loop counts as a second of time.
while len(active) < 26:
    # puts as many people to work as possible (and available)
    while len(runningTasks.keys()) < WORKERS:
        # print(len(runningTasks.keys()))
        next = getNextAvailable(runningTasks)
        if next is None:
            # print("nothing available")
            break
        else:
            nextChr = str.lower(next)
            # print( "starting: "+next, 60 + ( ord(nextChr) - 96 ) )
            runningTasks[next] = 60 + ( ord(nextChr) - 96 )

    # update time
    totalTime += 1

    # run active tasks (diminish time left by 1)
    for t in runningTasks.keys():
        runningTasks[t] -= 1
        if runningTasks[t] == 0:    #task is done, so add it to active set
            # print( "completed "+t )
            active.add(t)
            order += t

    # Remove all completed tasks from running (timeleft = 0)
    #  We do this outside of above loop to avoid changing the size while iterating
    #   plus, it gives me a reason to use this selection syntax again!
    runningTasks = {key: val for key, val in runningTasks.items() if val > 0}

print(totalTime, order)
