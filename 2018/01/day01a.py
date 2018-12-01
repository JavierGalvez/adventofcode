input = [int(line) for line in open('input.txt')]
val = 0
for frequency in input:
	val = val + frequency
print(val)
