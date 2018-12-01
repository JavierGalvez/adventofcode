def firstPart(steps):
    pos = 0
    circular = [0]
    for i in range(1,2018):
        pos = (pos + steps) % len(circular) + 1
        circular.insert(pos, i)
    return circular[pos+1]

def secondPart(steps):
    pos = 0
    for i in range(1,50000001):
        pos = (pos + steps) % i + 1
        if pos == 1:
            val = i
    return val

steps = 344
print('First part:', firstPart(steps))
print('Second part:', secondPart(steps))
