with open('day6.txt') as file:
    groups = file.read().split('\n\n')

# Part One
result1 = 0
for group in groups:
    list = []
    for letter in group:
        if letter not in list and letter != '\n':
            list.append(letter)
    result1 += len(list)

print(f'Part One answer is {result1}')

# Part Two
result2 = 0
for group in groups:
    tempList = group.split('\n')
    lengthTempList = len(tempList)
    comparer = set(tempList[0])
    for i in range(lengthTempList-1):
        comparer = comparer.intersection(set(tempList[i + 1]))
    
    result2 += len(comparer)

print(f'Part 2 answer is {result2}')