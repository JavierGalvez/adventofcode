data = input()
data = [ (line[0], int(line[1:])) for line in data.split("\n") ]
          
directions = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
turn = {"L": (-1, 1), "R": (1, -1)}

def move(p, d, units):
    return (p[0]+d[0]*units, p[1]+d[1]*units)

def rotate(p, r):
    return (p[1]*r[0], p[0]*r[1])

def run(ship, reference, part):
    for action, value in data:
        
        if action == "L" or action == "R":
            for i in range(value // 90):
                reference = rotate(reference, turn[action])
                
        elif action == "F":
            ship = move(ship, reference, value)
            
        else:
            if part == 1:
                ship = move(ship, directions[action], value)
            elif part == 2:
                reference = move(reference, directions[action], value)
                
    return abs(ship[0]) + abs(ship[1])

print("Part 1: %d" % run((0, 0), (0, 1), 1))
print("Part 2: %d" % run((0, 0), (-1, 10), 2))
