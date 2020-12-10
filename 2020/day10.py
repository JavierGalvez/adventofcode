from more_itertools import run_length
from functools import reduce

data = input()
data = sorted(list(map(int, data.split("\n"))))

data = [0] + data + [data[-1]+3]
diffs = [x-y for x, y in zip(data[1:], data)]
swap = {2: 2, 3: 4, 4: 7}

print("Part 1: %d" % (diffs.count(1) * diffs.count(3)))
print("Part 2: %d" % reduce(lambda x, y: x*y, [swap[n] for i, n in run_length.encode(diffs) if i == 1 and n > 1]))