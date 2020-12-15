data = input()
data = list(map(int, data.split(",")))

def run(data, n):
    spoken = {x: i for i, x in enumerate(data, start=1)}
    
    last = data[-1]
    for i in range(len(data), n):
        if last in spoken:
            spoken[last], last = i, i - spoken[last]
        else:
            spoken[last], last = i, 0
    return last

print("Part 1: %d" % run(data, 2020))
print("Part 2: %d" % run(data, 30000000))