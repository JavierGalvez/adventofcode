f = open('data.txt', 'r')
lines = [line.split(': ') for line in f]

layers = {int(pos): int(val) for pos, val in lines}

def firstPart():
    caughtBy = set()
    for pos in layers:
        if not pos % ((layers[pos] - 1) * 2):
            caughtBy.add(pos)

    return sum(k * layers[k] for k in caughtBy)

def secondPart():
    for i in range(2, 10**10):
        caught = False
        for pos in layers:
            if not (pos + i) % ((layers[pos] - 1) * 2):
                caught = True
                break
        if not caught:
            return i

print('First part:', firstPart())
print('Second part:', secondPart())
