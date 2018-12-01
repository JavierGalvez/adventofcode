input = [int(line) for line in open('input.txt')]
val = 0
vistos = set()
continuar = True
while continuar:
	for frequency in input:
		val = val + frequency
		if val in vistos:
			continuar = False
			break
		vistos.add(val)
print(val)
