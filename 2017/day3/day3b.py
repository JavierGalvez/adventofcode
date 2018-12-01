def sum(x,y):
    for j in range(x-1,x+2):
        for k in range(y-1,y+2):
            if(j >= 0 and j < n and k >= 0 and k < n):
                if(x != j or y != k):
                    spiral[x][y] += spiral[j][k]

n = 9
spiral = [[0 for i in range(n)] for j in range(n)]

x = y = int(n/2)
spiral[x][y] = 1

val = 277678

for i in range(1,int(n/2)+1):
    y += 1
    for k in range(0,2*i):
        xoff = -k
        sum(x+xoff,y)
        if(spiral[x+xoff][y] > val):
            break
    x += xoff
    if(spiral[x][y] > val):
        break
    for k in range(1,2*i+1):
        yoff = -k
        sum(x,y+yoff)
        if(spiral[x][y+yoff] > val):
            break
    y += yoff
    if(spiral[x][y] > val):
        break
    for k in range(1,2*i+1):
        xoff = k
        sum(x+xoff,y)
        if(spiral[x+xoff][y] > val):
            break
    x += xoff
    if(spiral[x][y] > val):
        break
    for k in range(1,2*i+1):
        yoff = k
        sum(x,y+yoff)
        if(spiral[x][y+yoff] > val):
            break
    y += yoff
    if(spiral[x][y] > val):
        break

print(spiral[x][y])
