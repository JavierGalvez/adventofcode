import re

f = open('data.txt', 'r')
data = []

for lines in f:
    string = lines.replace('\n','').replace('(','').replace(')','')
    string = re.split(r' -> |, | ',string)
    string[1] = int(string[1])
    data.append(string)

def firstPart(data):
    row = data[0]
    node = row[0]

    i = 0
    while i < len(data):
        if(data[i] != row and node in data[i]):
            row = data[i]
            node = row[0]
            i = 0
        else:
            i += 1
    return node

def weightR(node, tree):
    sumWeight = 0
    if(len(tree[node]) == 2):
        for i in range(len(tree[node][1])):
            sumWeight += weightR(tree[node][1][i],tree)
        sumWeight += tree[node][0]
    else:
        sumWeight += tree[node][0]
    return sumWeight

def secondPart(data, node):
    tree = {}
    for rows in data:
        tree[rows[0]] = [rows[1]]
        if(len(rows) > 2):
            tree[rows[0]].append(rows[2:])
    repeated = []
    while node not in repeated:
        repeated.append(node)
        weight = weightR(tree[node][1][0],tree)
        for sons in tree[node][1]:
            weight_to_compare = weightR(sons,tree)
            if(weight != weight_to_compare):
                node = sons

    for children in tree[repeated[repeated.index(node)-1]][1]:
        if(children != node):
            weight = weightR(children,tree)
            break
    return tree[node][0] - abs(weight - weightR(node,tree))

root = firstPart(data)
print("First part:",root)
print("Second part:",secondPart(data,root))
