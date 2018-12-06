f = open('input5.txt')
text = f.read()

# builds reagent list
input = []
for i in range(97, 97+26):
    input.append(chr(i) + str.upper((chr(i))))
    input.append(str.upper((chr(i))) + chr(i))

print(input)

# reacts string until length no longer changes
def resolve(inputText):
    curLen = 0
    while curLen != len(inputText):
        curLen = len(inputText)
        for key in input:
            inputText = inputText.replace(key, '')
    return inputText

# puzzle 1
output = resolve(text)
print(output)
print(len(output))

mostProblematic = ""
mostProblematicCount = len(text)

# parse collapsed variant after removing each individual reagent letter
for i in range(0, len(input), 2):   # skip reverse capitalized reagents
    alteredInput = text.replace(input[i][0], '')
    alteredInput = alteredInput.replace(input[i][1], '')
    output = resolve(alteredInput)
    if len(output) < mostProblematicCount:
        mostProblematicCount = len(output)
        mostProblematic = input[i]

# puzzle 2
print(mostProblematic, mostProblematicCount)
