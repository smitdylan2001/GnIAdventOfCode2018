from operator import itemgetter

# stores id and how often specific minutes were spent asleep
class Guard:
    def __init__(self, id):
        self.id = id
        self.minutes = {}
        for i in range(60):
            self.minutes[i] = 0

    def asleepAtMinute(self, minute):
        self.minutes[minute] += 1

    def printMinutes(self):
        print(self.minutes.values())

    def highestMinute(self):
        highest = -1
        highestIndex = 0
        curIndex = 0
        for i in self.minutes.values():
            if i > highest:
                highestIndex = curIndex
                highest = i
            curIndex += 1
        return [highest, highestIndex]

    def totalMinutes(self):
        minute = 0
        for i in self.minutes.values():
            minute += i
        return minute

    def getId(self):
        return self.id

# returns list of ints per line [year, month, day, hour, minute, act, id]
def parseLine(line):
    dateTime = line.split(']')[0]
    act = line.split(']')[1][1:]
    date = dateTime.split(' ')[0][1:]
    time = dateTime.split(' ')[1]
    id = -1

    if act[0] == 'f':
        act = ACT_SLEEP
    elif act[0] == 'w':
        act = ACT_WAKE
    elif act[0] == 'G':
        id = act.split('#')[1]
        id = int(id.split(' ')[0])
        act = ACT_GUARD

    # parse year, month, day, hour minute
    year = int(date.split('-')[0])
    month = int(date.split('-')[1])
    day = int(date.split('-')[2])
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])

    return [ year, month, day, hour, minute, act, id]

# named values to keep things readable
YEAR = 0
MONTH = 1
DAY = 2
HOUR = 3
MINUTE = 4
ACT = 5
ID = 6

ACT_SLEEP = 0
ACT_WAKE = 1
ACT_GUARD = 2

# stores guard instances by id
guards = {}

f = open('input4.txt')
lines = f.readlines()

# parse lines into events
events = []
for line in lines:
    data = parseLine(line)
    events.append(data)

# sort data based on date & time
events = sorted(events, key=itemgetter(YEAR, MONTH, DAY, HOUR, MINUTE))

activeGuard = -1
asleep = False
startMinutes = -1
for e in events:
    # parse sorted events into Guard data
    if e[ACT] == ACT_GUARD:
        activeGuard = e[ID]
        if e[ID] not in guards.keys():
            guards[e[ID]] = Guard(e[ID])
    elif e[ACT] == ACT_SLEEP:
        startMinutes = e[MINUTE]
    elif e[ACT] == ACT_WAKE:
        # since its now sorted, we can calculate end minutes
        #  we're assming (based on requirements) that this never exceeds the minute boundary
        endMinutes = e[MINUTE]
        for m in range(startMinutes,endMinutes):
            guards[activeGuard].asleepAtMinute(m)


highestTotal = 0
highest = 0
highestId = 0
highestMinute = 0
for guard in guards.values():
    if guard.totalMinutes() > highestTotal:
        stats = guard.highestMinute()
        highestTotal = guard.totalMinutes()
        highest = stats[0]
        highestMinute = stats[1]
        highestId = guard.getId()

print("value, minute, guardId: ", highest, highestMinute, highestId)
print(highestMinute * highestId)

highest = 0
highestMinute = 0
for guard in guards.values():
    stats = guard.highestMinute()
    if stats[0] > highest:
        highest = stats[0]
        highestMinute = stats[1]
        highestId = guard.getId()
print("guardId, highestMinute, highestValue", highestId, highestMinute, highest)
print(highestId * highestMinute)
