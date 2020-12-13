from math import prod

data = input()
data = data.split("\n")

depart = int(data[0])
bus = [ (int(x), i) for i, x in enumerate(data[1].split(",")) if x != "x" ]

bus = sorted(bus, reverse=True)
increment, t = 1, 0

for b, offset in bus:
    while True:
        if (t + offset) % b == 0:
            increment *= b
            break
        else:
            t += increment
            
print("Part 1: %d" % prod(min([ (b - depart % b, b) for b, offset in bus ])))
print("Part 2: %d" % t)