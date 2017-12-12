f = open('data.txt')
moves = f.readline().replace('\n','').split(',')

x = 0
y = 0

furthest = 0

for move in moves:
    if move == 'n':
        y += 1
    elif move == 'ne':
        x += 0.5
        y += 0.5
    elif move == 'nw':
        x -= 0.5
        y += 0.5
    elif move == 'se':
        x += 0.5
        y -= 0.5
    elif move == 'sw':
        x -= 0.5
        y -= 0.5
    else:
        y -= 1

    if abs(x) + abs(y) > furthest:
        furthest = abs(x) + abs(y)

print('First part:',abs(x) + abs(y))
print('Second part:',furthest)
