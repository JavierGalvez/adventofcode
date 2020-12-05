data = input()
data = data.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1").split("\n")

ids = sorted([int(line[:7], 2)*8 + int(line[7:], 2) for line in data])

print("Part 1: %d" % ids[-1])
print("Part 2: %d" % next(i+1 for i in ids if i+1 not in ids))