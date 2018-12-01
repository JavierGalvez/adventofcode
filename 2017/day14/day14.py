def knothash(string):
    numbers = [ i for i in range(256)]
    asciicode = []
    for characters in string:
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

def firstPart(string):
    used = 0
    ret = []
    for i in range(128):
        hash = knothash(string + '-' + str(i))
        binHash = bin(int(hash,16))[2:].zfill(128)
        ret.append(list(binHash))
        used += sum(int(k) for k in binHash)
    return (used, ret)

def regions(x, y, grid):
    if grid[x][y] == '0':
        return
    grid[x][y] = '0'
    if x > 0:
        regions(x-1, y, grid)
    if x + 1 < 128:
        regions(x+1, y, grid)
    if y > 0:
        regions(x, y-1, grid)
    if y + 1 < 128:
        regions(x, y+1, grid)


def secondPart(grid):
    count = 0
    for i in range(128):
        for j in range(128):
            if grid[i][j] == '1':
                regions(i,j,grid)
                count += 1
    return count;


input = 'jxqlasbh'
used, grid = firstPart(input)
print('First part:', used)
print('Second part:', secondPart(grid))
