
def firstPart():
    numbers = [ i for i in range(256)]
    lengths = [199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192]

    skip = pos = 0

    for l in lengths:
        if pos + l > len(numbers):
            dif = pos + l - len(numbers)
            sub = numbers[pos:256] + numbers[0:dif]
        else:
            sub = numbers[pos:pos+l]
        sub = sub[::-1]
        for n in sub:
            numbers[(pos + sub.index(n)) % len(numbers)] = n
        pos = (pos + l + skip) % len(numbers)
        skip += 1
    return (numbers[0] * numbers[1])

def secondPart():
    numbers = [ i for i in range(256)]
    lengths = '199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192'
    asciicode = []
    for characters in lengths:
        asciicode.append(ord(characters))
    asciicode += [17,31,73,47,23]
    pos = skip = 0
    for _ in range(64):
        for l in asciicode:
            if pos + l > 256:
                sub = numbers[pos:256] + numbers[0:pos + l - 256]
            else:
                sub = numbers[pos:pos+l]
            sub = sub[::-1]
            for n in sub:
                numbers[(pos + sub.index(n)) % 256] = n
            pos = (pos + l + skip) % 256
            skip += 1

    denseHash = []
    for i in range(16):
        xor = numbers[16 * i]
        for n in numbers[16 * i + 1: 16 * i + 16]:
            xor ^= n
        denseHash.append(format(xor, '02x'))

    return ''.join(denseHash)

print('First part:',firstPart())
print('Second part:',secondPart())
