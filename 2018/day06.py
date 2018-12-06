from collections import defaultdict

input = [ tuple(map(int, l.replace('\n', '').split(', '))) for l in open('inputs/6.txt') ] 

def manhattan (a, b):
   return abs(a[0] - b[0]) + abs(a[1] - b[1])

max_x = max(input)[0] + 1 
max_y = max(input, key=lambda a: a[1])[1] + 1

infinite = {(-1, -1)}
grid = {}
areas = defaultdict(int)
save_region = []

for x in range(max_x):
   for y in range(max_y):
      distances = [manhattan((x,y), point) for point in input]
      if sum(distances) < 10000:
         save_region.append((x, y))

      shortest_dist = min(distances)
      closest_points = [ point for i, point in enumerate(input) if distances[i] == shortest_dist ]

      if len(closest_points) != 1:
         grid[(x, y)] = (-1, -1)
      else:
         grid[(x, y)] = shortest_dist
         areas[closest_points[0]] += 1

      if x == 0 or y == 0 or x == max_x or y == max_y:
         for points in closest_points:
            infinite.add(points)

print('Part 1:', max(areas.items(), key=lambda a: a[1] if a[0] not in infinite else 0)[1])
print('Part 2:', len(save_region))
