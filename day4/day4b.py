f = open('data.txt', 'r')
data = [ map(sorted,line.replace('\n', '').split(' ')) for line in f ]

n = 0
for lines in data:
    finePP = 1
    for i in range(len(lines)):
        for j in range(len(lines)):
            if(i!=j and lines[i] == lines[j]):
                finePP = 0
                break
    n += finePP
print(n)
