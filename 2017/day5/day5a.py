data = [int(line) for line in open('data.txt')]

index = 0
steps = 0

while index < len(data):
    data[index] += 1
    index += data[index] - 1
    steps += 1
print(steps)
