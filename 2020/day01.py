from itertools import combinations
from functools import reduce

data = input()
data = list(map(int, data.split("\n")))
    
def compute(data, n):
    for c in combinations(data, n):
        if sum(c) == 2020:
            return reduce(lambda x,y: x*y, c)

print("Part 1: %d" % compute(data, 2))
print("Part 2: %d" % compute(data, 3))