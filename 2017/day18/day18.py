f = open('data.txt', 'r')
instructions = [ lines.replace('\n','').split(' ') for lines in f ]

def setreg (a, b):
    if b.isdigit():
        registers[a] = int(b)
    else:
        registers[a] = int(registers[b])

def addreg (a, b):
    if b.isdigit():
        registers[a] += int(b)
    elif b[1:].isdigit():
        registers[a] += - int(b[1:])
    else:
        registers[a] += int(registers[b])

def mulreg (a, b):
    if b.isdigit():
        registers[a] *= int(b)
    elif b[1:].isdigit():
        registers[a] *= - int(b[1:])
    else:
        registers[a] *= int(registers[b])

def modreg (a, b):
    if b.isdigit():
        registers[a] %= int(b)
    elif b[1:].isdigit():
        registers[a] %= - int(b[1:])
    else:
        registers[a] %= int(registers[b])

def snd (a):
    global send
    if a.isdigit():
        send.append(int(a))
    else:
        send.append(int(registers[a]))
    return None

def rcv (a):
    global send
    if a.isdigit():
        if a > 0:
            return send.pop()
    elif registers[a] > 0:
            return send.pop()
    return None

def jgz (a, b):
    global pos
    if b.isdigit():
        jump = int(b)
    elif b[1:].isdigit():
        jump = - int(b[1:])
    else:
        jump = int(registers[b])

    if a.isdigit():
        if a > 0:
            pos = pos + jump - 1
    else:
        if registers[a] > 0:
            pos = pos + jump - 1

ops = { "set": setreg,
        "add": addreg,
        "mul": mulreg,
        "mod": modreg,
        "snd": snd,
        "rcv": rcv,
        "jgz": jgz}

registers = {}
send = []
pos = 0

def firstPart():
    global pos
    ret = None
    while pos < len(instructions):
        row = instructions[pos]
        if row[1] not in registers:
            registers[row[1]] = 0

        if len(row) == 2:
            ret = ops[row[0]](row[1])
        if len(row) == 3:
            ops[row[0]](row[1],row[2])
        pos += 1
        print(registers)
        if ret is not None:
            break
    return ret

print('First part:', firstPart())
