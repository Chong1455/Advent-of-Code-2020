from copy import deepcopy

seats = []

with open('day11.txt') as file:
    for line in file:
        seats.append(list(line.rstrip()))

row = len(seats)
col = len(seats[0])

def check_valid_seat(i, j):
    if i < 0 or j < 0 or i >= row or j >= col:
        return False
    return True

def check_adjacent_seats(i, j, grid, part):
    x = [-1, 0, 1, -1, 1, -1, 0, 1]
    y = [1, 1, 1, 0, 0, -1, -1, -1]
    occupied = 0
    for k in range(8):
        adj_i = i + x[k]
        adj_j = j + y[k]
        while check_valid_seat(adj_i, adj_j) and grid[adj_i][adj_j] == '.' and part == 2:
            adj_i += x[k]
            adj_j += y[k]
        if check_valid_seat(adj_i, adj_j) and grid[adj_i][adj_j] == '#':
            occupied += 1
    return occupied

def solve(grid, part):
    while True:
        change = False
        new_grid = deepcopy(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'L' and check_adjacent_seats(i, j, grid, part) == 0:
                    new_grid[i][j] = '#'
                    change = True
                elif grid[i][j] == '#' and check_adjacent_seats(i, j, grid, part) >= (4 if part == 1 else 5):
                    new_grid[i][j] = 'L'
                    change = True
                else:
                    new_grid[i][j] = grid[i][j]
        grid = deepcopy(new_grid)
        if not change:
            print(sum(rows.count('#') for rows in grid))
            return

solve(seats, 1) # Part One
solve(seats, 2) # Part Two