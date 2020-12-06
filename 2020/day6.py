from functools import reduce

data = input()
data = data.split("\n\n")

print("Part 1: %d" % sum([len(set(g.replace("\n", ""))) for g in data]))
print("Part 2: %d" % sum([len(reduce(set.intersection, map(set, g.split("\n")))) for g in data]))