data = input()
data = data.split("\n")

valid1 = valid2 = 0
for line in data:
    p, pw = line.split(':')
    r, l = p.split(' ')
    x, y = map(int, r.split('-'))
    
    count = pw.count(l)
    if count >= x and count <= y:
        valid1 += 1
        
    if (pw[x] == l and pw[y] != l) or (pw[x] != l and pw[y] == l):
        valid2 += 1
          
print("Part 1: %d" % valid1)
print("Part 2: %d" % valid2)