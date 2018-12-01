f = open('data.txt', 'r')
numbers = [ list(map(int,line.replace('\n', '').split('\t'))) for line in f ]

checksum = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            if((numbers[i][j] % numbers[i][k]) == 0 and j != k):
                checksum += numbers[i][j] / numbers[i][k]
print(checksum)
