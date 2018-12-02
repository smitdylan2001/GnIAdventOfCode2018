__author__ = 'aoostdijk'

from math import *


f = open("input_1.txt", 'r')

lines = f.readlines()

# brute force
def contains( value, list ):
    if value == 0: return True

    for i in list:
        if i == value:
            print("FOUND")
            return True
    return False


freq = 0
seenFreq = []

seenPos = []
seenNeg = []

seenDic = set([])

# looks for target in array, if it doesn't find it, it stores it in a sorted way
# I implemented this wrong I think because it always ends with one-value separation in the end
# hence the mess inside guess == min...
def binarySearchInsert(arr, target):
    min = 0
    max = len(arr)-1
    done = False

    # empty array, add target as first value
    if max == 0:
        if arr[0] < target:
            arr.append(target)
        else:
            arr.insert(0, target)
        return False

    while not done:
        guess = int(min + (max - min) * .5)

        # we've reached the point where only min and max are the remaining values
        # so either we find it, or we insert and break
        if guess == min:
            if arr[min] == target or arr[max] == target:
                return True
            else:
                # print(target)
                # print(min, max, guess)
                # print(arr[min], arr[max], arr[guess])
                if target > arr[max]:
                    index = max+1
                    if index >= len(arr):
                        arr.append(target)
                    else:
                        arr.insert(index, target)
                elif target < arr[min]:
                    index = min-1
                    if index < 0:
                        index = 0
                    arr.insert(index, target)
                else:
                    arr.insert(min+1, target)
                return False

        # found match
        if arr[guess] == target:
            return True
        else:
            if arr[guess] < target:
                min = guess
            else:
                max = guess

# insert target into arr such that arr[first..last] is sorted,
#   given that arr[first..last-1] is already sorted.
#   Return the position where inserted.
def orderedInsert (arr, target):
    arr.append(arr[-1]) # add target to end as starting position of new value
    i = len(arr)-1
    while (i > 0) and (target < arr[i-1]):
        arr[i] = arr[i-1]
        i = i - 1
    arr[i] = target

    #if we insert next to ourselves, we found it!
    if arr[i-1] == target:
        return True
    else:
        return False

# add first frequency (0)
seenFreq.append(freq)

running = True
loops = 0

while running:
    print("generation: "+str(loops))
    for line in lines:
        # get current change
        change = int(line)
        # alter frequence
        freq += change
        # insert sorted, check if we insert next to same value (True)
        if freq in seenDic:
            print("found recurring freq: "+str(freq))
            running = False
            break
        else:
            seenDic.add(freq)
        '''
        if binarySearchInsert(seenFreq, freq):
            print("found current freq: "+str(freq)+" in list")
            running = False
            break
        '''
    loops += 1

print(seenFreq)
print(str(freq))
