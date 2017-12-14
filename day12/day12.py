f = open('data.txt', 'r')
comunications = [list(map(int,lines.replace('\n','').split(' <-> ')[1].split(', '))) for lines in f]

grouped = [ 0 for i in range(len(comunications))]
IDs = []
for i in enumerate(grouped):
    if i[1] == 0:
        IDi = set()
        IDi.add(i[0])
        for j in comunications[i[0]]:
            IDi.add(j)
        aux = 0
        while len(IDi) != aux:
            aux = len(IDi)
            for j, programs in enumerate(comunications):
                if j in IDi:
                    for related in programs:
                        IDi.add(related)
        for k in enumerate(IDi):
            grouped[k[1]] = 1
        IDs.append(IDi)

print('First part:',len(IDs[0]))
print('Second part:',len(IDs))
