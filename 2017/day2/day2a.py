f = open('data.txt', 'r')
numbers = [ list(map(int,line.replace('\n', '').split('\t'))) for line in f ]

checksum = 0;
for rows in numbers:
    checksum += max(rows) - min(rows)
print(checksum)
