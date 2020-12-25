with open('day13.txt') as file:
    data = file.read().splitlines()

timestamp = int(data[0])
busses = [int(l) if l !='x' else None for l in data[1].split(',')]

# Part One
best_bus = None
min_wait_time = float('inf')

for bus in busses:
    if bus:
        wait_time = bus - timestamp % bus
        if min_wait_time > wait_time:
            best_bus = bus
            min_wait_time = wait_time

print('Part One answer is ', best_bus * min_wait_time)

# Part Two

bus_ids = tuple((int(bus), (int(bus) - i) % int(bus)) for i, bus in enumerate(busses) if bus)
tmp = bus_ids[0][0]
timestamp, i = tmp, 0

# Chinese Remainder Theorem

loop = True
while loop:
  bus, remainder = bus_ids[i+1]
  if (timestamp) % bus  == remainder:
    if i == len(bus_ids) - 2:
      print(f"Part Two answer: {timestamp}")
      loop = False
    tmp *= bus
    i += 1
  timestamp += tmp