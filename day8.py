with open('day8.txt') as f:
    data = f.read().strip().split('\n')

for i in range(len(data)):
    data[i] = data[i].split()
    data[i][1] = int(data[i][1])

traversed = list()
acc = 0

# Part One
def loop(data, i=0):
    global acc
    if i not in traversed:
        traversed.append(i)
        if data[i][0] == 'acc':
            acc += data[i][1]
            return loop(data, i+1)
        elif data[i][0] == 'nop':
            return loop(data, i+1)
        elif data[i][0] == 'jmp':
            return loop(data, i+data[i][1])
    return acc

print('Part One answer is', loop(data))

# Part Two
traversed_jmp_nop = list()
for i in traversed:
    if data[i][0] == 'jmp' or data[i][0] == 'nop':
        traversed_jmp_nop.append(i)

def loop2(data, i=0):
    for j in traversed_jmp_nop:
        traversed = list()
        acc = 0
        i = 0
        k = 0
        def loop(data, i):
            nonlocal acc
            if i >= len(data):
                nonlocal k
                k = i
                return
            if i not in traversed:
                traversed.append(i)
                if data[i][0] == 'acc':
                    acc += data[i][1]
                    return loop(data, i+1)
                elif data[i][0] == 'nop':
                    if i==j:
                        return loop(data, i+data[i][1])
                    return loop(data, i+1)
                elif data[i][0] == 'jmp':
                    if i==j:
                        return loop(data, i+1)
                    return loop(data, i+data[i][1])
            return
        loop(data, i)
        if k >= len(data):
            return acc

print('Part Two answer is', loop2(data))