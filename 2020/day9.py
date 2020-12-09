from itertools import combinations

data = input()
data = list(map(int, data.split("\n")))

def part2(data, val):
    for i, x in enumerate(data):
        s = x
        for j, y in enumerate(data[i+1:], start=i+1):
            s += y
            if s == val:
                return min(data[i:j+1]) + max(data[i:j+1])
            elif s > val:
                break

n = 25
first = next(k for i, k in enumerate(data[n:], start=n) if all(k != x+y for x,y in combinations(data[i-n:i], 2)))

print("Part 1: %d" % first)
print("Part 2: %d" % part2(data, first))
