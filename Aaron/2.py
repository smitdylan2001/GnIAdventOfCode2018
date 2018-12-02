__author__ = 'aoostdijk'

f = open('input_2.txt', 'r')
lines = f.readlines()

twiceCount = 0
thriceCount = 0

for boxID in lines:
    # store letters we've seen in a unique set
    letters = set()
    # store how often we've seen each letter in a dictionary
    letterCounts = {}

    # bools to store if words count towards each case
    # to prevent counting repeats (lots of double letters apparently)
    Two = False
    Three = False

    # parse for duplicates / triplicates
    for i in boxID:
        if i in letters:
            letterCounts[i] += 1
        else:
            letterCounts[i] = 1
        letters.add(i)

    # check if we have duplicates / triplicates
    for x in letterCounts.keys():
        if letterCounts[x] == 3:
            Three = True
        elif letterCounts[x] == 2:
            Two = True

    # add to respective counts
    if Two:     twiceCount += 1
    if Three:   thriceCount += 1

print("checksum: "+ str(twiceCount*thriceCount))

# cross-reference each boxID
for i in  range(len(lines)):
    # guarantee single handshake
    for j in range(i + 1, len(lines)):
        # create variants at each index for both strings and compare them
        for x in range(len(lines[i])):
            # remove same index from each string
            stri = lines[i][:x] + lines[i][x+1:]
            strj = lines[j][:x] + lines[j][x+1:]

            # for answer this should then be equal
            if stri == strj:
                print("Found candidate! Common string: "+stri, i, j)
