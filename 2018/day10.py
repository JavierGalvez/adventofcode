from re import findall

points = [ tuple(map(int, findall(r'-?\d+', l))) for l in open('inputs/10.txt') ]

box = (999999, -1)

for time in range(15000):
	x, y, vx, vy = points[0]
	min_x = max_x = x + vx * time
	min_y = max_y = y + vy * time
	for x, y, vx, vy in points[1:]:
		min_x = min(min_x, x + vx * time)
		max_x = max(max_x, x + vx * time)
		min_y = min(min_y, y + vy * time)
		max_y = max(max_y, y + vy * time)
	area = max_x - min_x + max_y - min_y
	if area < box[0]:
		box = (area, min_x, max_x, min_y, max_y, time)

_, min_x, max_x, min_y, max_y, time = box
message = [ [' '] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1) ]
for x, y, vx, vy in points:
	message[y+vy*time-min_y][x+vx*time-min_x] = '#'

print('Part 1:')
for row in message:
	print(''.join(row))
print('Part 2:', time)
