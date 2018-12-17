from datetime import datetime
import re
import operator

SLEEP = 1
WAKE = 2
SHIFT = 3

def solve(input):
    events = []

    with open(input) as f:
        for line in f:
            d = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
            e = 0
            id = -1
            if line.endswith("asleep\n"):
                e = SLEEP
            elif line.endswith("up\n"):
                e = WAKE
            elif line.endswith("shift\n"):
                e = SHIFT
                matches = re.findall(r'[0-9]+', line)
                id = int(matches[-1])
            else:
                print("Error: " + line)
                continue

            events.append({ 'timestamp': d, 'event': e, 'id': id })

    events.sort(key=operator.itemgetter('timestamp'))

    guards = {}
    currentGuard = -1
    sleepStart = -1
    for event in events:
        if event['event'] == SHIFT:
            currentGuard = event['id']
            if not currentGuard in guards:
                guards[currentGuard] = { 'sleep': [0 for i in range(60)] }
        elif event['event'] == SLEEP:
            sleepStart = event['timestamp'].minute
        elif event['event'] == WAKE:
            sleepEnd = event['timestamp'].minute
            for i in range(sleepStart, sleepEnd):
                guards[currentGuard]['sleep'][i] += 1

    chosenGuard = -1
    chosenMinute = -1
    highest = -1
    for guardID, guard in guards.items():
        for minute in range(len(guard['sleep'])):
            if guard['sleep'][minute] > highest:
                chosenGuard = guardID
                chosenMinute = minute
                highest = guard['sleep'][minute]

    print(chosenGuard * chosenMinute)

solve("../input.txt")