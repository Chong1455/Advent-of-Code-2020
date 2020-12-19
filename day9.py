f = open('day9.txt')
data = list(map(int, f.read().split('\n')))
start = 0
end = 25

# Part One
def check_valid(num, arr):
    for i in arr:
        if (num-i) in arr:
            return True
    return False

invalid = -1
while start < len(data)-end:
    next = data[end]
    if check_valid(next, data[start:end]) == False:
        invalid = next
        break
    start += 1
    end += 1

print(f'Part One answer is {invalid}')

# Part Two
index = 0
start = 0
total = 0
while start < len(data):
    total += data[index]
    index += 1
    if total > invalid:
        start += 1
        index = start
        total = 0
    elif total == invalid:
        break

contuguous = data[start:index]
 
low = min(contuguous)
high = max(contuguous)
s = low + high

print(f'Part Two answer is {s}')