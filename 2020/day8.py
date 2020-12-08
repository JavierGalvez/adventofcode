data = input()
data = [ (line[:3], int(line[4:])) for line in data.split("\n") ]

def run(data):
    index = 0
    accumulator = 0
    seen = set()
    
    while index not in seen and index < len(data):
        seen.add(index)
        action, n = data[index]
        if action == "acc": accumulator += n
        elif action == "jmp": index += n - 1
        index += 1

    return index, accumulator

def part2(data):
    swap = {"jmp": "nop", "nop": "jmp"}
    
    for i, (action, n) in enumerate(data):
        if action == "jmp" or action == "nop":
            index, accumulator = run(data[:i] + [(swap[action], n)] + data[i+1:])
            if index >= len(data): return accumulator
            
    return -1

print("Part 1: %d" % run(data)[1])
print("Part 2: %d" % part2(data))