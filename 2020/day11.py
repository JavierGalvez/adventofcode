from copy import deepcopy

data = input()
data = data.split("\n")

def in_bounds(x, y):
    return (x >= 0 and x < len(data)) and (y >= 0 and y < len(data[0]))

adjacents = dict()
for x in range(len(data)):
    for y in range(len(data[0])):
        adjacents[(x, y)] = [(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2) 
                             if in_bounds(i, j) and not (i == x and j == y)]

def check_adjacents(x, y, data):
    return sum(1 for i, j in adjacents[(x, y)] if data[i][j] == "#")

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]

def check_in_sight(x, y, data):
    in_sight = 0
    for dir_x, dir_y in directions:
        check_x, check_y = x + dir_x, y + dir_y
        
        while in_bounds(check_x, check_y):
            if data[check_x][check_y] == "L":
                break
            elif data[check_x][check_y] == "#":
                in_sight += 1
                break
            
            check_x += dir_x
            check_y += dir_y
            
    return in_sight  
    
    
def occupied_seats(data, func_occupied, max_occupied):
    swap = {"#": "L", "L": "#"}
    aux = deepcopy(data)
    change = True
    while change:
        change = False
        for i, line in enumerate(data):
            for j, seat in enumerate(line):
                occupied = func_occupied(i, j, data)
                if (occupied == 0 and seat == "L") or (occupied >= max_occupied and seat == "#"):
                    aux[i] = aux[i][:j] + swap[seat] + aux[i][j+1:]
                    change = True
        data = deepcopy(aux)
        
    return sum(map(lambda x: x.count("#"), data))

print("Part 1: %d" % occupied_seats(data, check_adjacents, 4))
print("Part 2: %d" % occupied_seats(data, check_in_sight, 5))