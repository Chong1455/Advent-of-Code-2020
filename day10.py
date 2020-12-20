from collections import defaultdict

with open('day10.txt') as f:
    adapters = list(map(int, f.read().splitlines()))

# Part One
adapters.sort()
adapters.append(adapters[-1]+3)

init = one = three = 0

for adapter in adapters:
    diff = adapter - init
    if diff == 1:
        one += 1
    if diff == 3:
        three += 1
    init = adapter

print(f'Part One answer is {one*three}')

# Part Two
options = defaultdict(int)
options[0] = 1
for i in adapters:
    options[i] = sum([options[i-d] for d in [1,2,3]])

print(f'Part Two answer is {options[adapters[-1]]}')