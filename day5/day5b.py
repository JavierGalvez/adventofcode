data = [int(line) for line in open('data.txt')]

index = 0
steps = 0

while index < len(data):
    increment = 1
    if(data[index] >= 3):
        increment = -1
    data[index] += increment
    index += data[index] - increment
    steps += 1
print(steps)
