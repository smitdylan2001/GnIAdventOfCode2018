__author__ = 'aoostdijk'

input = 894501

recipeList = [3,7]
active1 = 0
active2 = 1

def update(count, list):
    count = ( count + list[count] + 1 ) % len(list)
    return count

def step():
    global active1, active2, recipeList
    # get sum of current
    sumCurrent = recipeList[active1] + recipeList[active2]

    # update list
    if sumCurrent >= 10:
        two = sumCurrent % 10
        one = int( sumCurrent / 10 )
        recipeList.append(one)
        recipeList.append(two)
    else:
        recipeList.append(sumCurrent)

    # update positions
    active1 = update(active1, recipeList)
    active2 = update(active2, recipeList)

# puzzle 1
'''
for i in range(0,input+10):
   step()

output = ""
for i in range(input, input+10):
    output += str(recipeList[i])

print(output)
'''

# puzzle 2

strInput = str(input)
lenInput = len(strInput)
intInput = int(input)
found = False
lastMax = 0
while not found:
    # print(lastMax)
    if lastMax % 10000 == 0:
        print(lastMax)
    step()
    for i in range(lastMax, len(recipeList)-lenInput):
        a = map(str, recipeList[i:i+lenInput])
        a = int(''.join(a))
        lastMax = i
        if a == intInput:
            print( "FOUND IT: "+str(i))
            found = True
            break


