from collections import Counter

input = [line.replace('\n','') for line in open('inputs/2.txt')]

twice, threeTimes = 0, 0
for row in input:
   count = {n for i, n in Counter(row).most_common()}
   if 2 in count:
      twice += 1
   if 3 in count:
      threeTimes += 1

print('Part 1:', twice * threeTimes)

for k, r1 in enumerate(input):
   for r2 in input[k+1:]:
      diff = 0
      for i, j in zip(r1, r2):
         if i != j:
            diff += 1
      if diff == 1:
         print('Part 2:', ''.join([i for i, j in zip(r1, r2) if i == j]))
