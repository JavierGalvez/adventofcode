from collections import defaultdict
input = [line.replace('@', '').split() for line in open('input.txt')]

for i, claim in enumerate(input):
   id = int(claim[0][1:])
   loff, toff = map(int, claim[1][:-1].split(','))
   width, height = map(int, claim[2].split('x'))
   input[i] = [id, loff, toff, width, height]

overlaps = defaultdict(int)
for claim in input:
   for i in range(claim[3]):
      for j in range(claim[4]):
         overlaps[(claim[1]+i, claim[2]+j)] += 1

ret = 0
for k, v in overlaps.items():
   if v > 1:
      ret += 1
print(ret)
