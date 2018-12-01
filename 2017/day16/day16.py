f = open('data.txt', 'r')
dance = f.readline().replace('\n', '').split(',')

def firstPart(string):
    programs = list(string)
    for moves in dance:
        if moves[0] == 's':
            i = int(moves[1:])
            programs = programs[-i:] + programs[:-i]
        elif moves[0] == 'x':
            i, j = map(int, moves[1:].split('/'))
            programs[i], programs[j] = programs[j], programs[i]
        else:
            i = programs.index(moves[1])
            j = programs.index(moves[3])
            programs[i], programs[j] = programs[j], programs[i]
    return ''.join(programs)


def secondPart(string):
    repeated = []
    for _ in range(1000000000):
        if string in repeated:
            break
        repeated.append(string)
        string = firstPart(string)
    return repeated[1000000000 % len(repeated)]

print('Fisrt part:', firstPart("abcdefghijklmnop"))
print('Second part:', secondPart("abcdefghijklmnop"))
