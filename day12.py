instructions = []

with open('day12.txt') as file:
    for line in file:
        instructions.append((line[0], int(line.rstrip()[1:])))

ord = {'N': 1, 'S': -1, 'E': 1, 'W': -1}
left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

# Part One
direction = 'E'
x = y = 0

for data in instructions:
    instruction, value = data
    if instruction == 'F':
        if direction == 'E' or direction == 'W':
            x += value * ord[direction]
        else:
            y += value * ord[direction]
    elif instruction == 'L':
        for _ in range(value // 90):
            direction = left[direction]
    elif instruction == 'R':
        for _ in range(value // 90):
            direction = right[direction]
    elif instruction == 'N' or instruction == 'S':
        y += value * ord[instruction]
    else:
        x += value * ord[instruction]

print('Part One answer is ', abs(x) + abs(y))

# Part Two
wx, wy = 10, 1
x = y = 0

for data in instructions:
    instruction, value = data
    if instruction == 'F':
        x += value * wx
        y += value * wy
    elif instruction == 'L':
        for _ in range(value // 90):
            wx, wy = -wy, wx
    elif instruction == 'R':
        for _ in range(value // 90):
            wx, wy = wy, -wx
    elif instruction == 'N' or instruction == 'S':
        wy += value * ord[instruction]
    else:
        wx += value * ord[instruction]

print('Part Two answer is ', abs(x) + abs(y))
            