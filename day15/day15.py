def generator1 (val, product):
    x = val
    while True:
        x = (x * product) % 2147483647
        yield x

def firstPart(A, B):
    count = 0
    for _ in range(40000000):
        a = next(A)
        b = next(B)
        if a & 0xFFFF == b & 0xFFFF:
            count += 1
    return count

def generator2 (val, product, k):
    x = val
    while True:
        x = (x * product) % 2147483647
        if not x % k:
            yield x

def secondPart(A, B):
    count = 0
    for _ in range(5000000):
        a = next(A)
        b = next(B)
        if a & 0xFFFF == b & 0xFFFF:
            count += 1
    return count

genA = generator1(634, 16807)
genB = generator1(301, 48271)
print('First part:', firstPart(genA, genB))

genA = generator2(634, 16807, 4)
genB = generator2(301, 48271, 8)
print('Second part:', secondPart(genA, genB))
