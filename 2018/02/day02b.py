input = [line for line in open('input.txt')]
ret = ''
for k, r1 in enumerate(input):
	for r2 in input[k+1:]:
		diff = 0
		for i, j in zip(r1, r2):
			if i != j:
				diff += 1
		if diff == 1:
				ret = ''.join([i for i, j in zip(r1, r2) if i == j])
print(ret)
