f = open('data.txt', 'r')
data = list(map(int, f.readline().replace('\n','').split('\t')))

string = ' '.join(map(str,data))
redistributions = []

steps = 0
while string not in redistributions:
    redistributions.append(string)
    maxBlocks = max(data)
    idx = data.index(maxBlocks)
    data[idx] = 0
    for i in range(1,maxBlocks+1):
        data[(idx+i)%len(data)] += 1
    steps += 1
    string = ' '.join(map(str,data))

print(steps-redistributions.index(string))
