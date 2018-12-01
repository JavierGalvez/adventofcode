import operator

f = open('data.txt', 'r')
data = [ list(map(str,lines.replace('\n','').split(' '))) for lines in f]

values = {}

for rows in data:
    values[rows[0]] = 0


ops = { "<": operator.lt,
        ">": operator.gt,
        "<=": operator.le,
        ">=": operator.ge,
        "!=": operator.ne,
        "==": operator.eq,
        "dec": operator.sub,
        "inc": operator.add}


maximum = 0

for rows in data:
    if(ops[rows[5]](values[rows[4]],int(rows[6]))):
        values[rows[0]] = ops[rows[1]](values[rows[0]],int(rows[2]))
        if(values[rows[0]] > maximum):
            maximum = values[rows[0]]

print("First part:",values[max(values.items(), key=operator.itemgetter(1))[0]])
print("Second part:",maximum)
