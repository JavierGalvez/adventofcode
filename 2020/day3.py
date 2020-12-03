from functools import reduce

data = input()
data = data.split("\n")

def count_trees(data, slope):
    return len([i for i, line in enumerate(data[::slope[0]]) if line[(i * slope[1]) % len(line)] == '#'])

print("Part 1: %d" % count_trees(data, (1, 3)))
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
print("Part 2: %d" % reduce(lambda x,y: x*y, [count_trees(data, slope) for slope in slopes]))