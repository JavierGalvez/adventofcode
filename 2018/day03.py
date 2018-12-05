from collections import defaultdict

claims = []
overlaps = defaultdict(int)

for claim in open('inputs/3.txt'):
   claim = claim.replace('@', '').split()
   identifier = int(claim[0][1:])
   loff, toff = map(int, claim[1][:-1].split(','))
   width, height = map(int, claim[2].split('x'))
   claims.append([identifier, loff, toff, width, height])

   for i in range(width):
      for j in range(height):
         overlaps[(loff+i, toff+j)] += 1

ret = 0
for k, v in overlaps.items():
   if v > 1:
      ret += 1
print('Part 1:', ret)

for claim in claims:
   no_overlap = True
   for i in range(claim[3]):
      for j in range(claim[4]):
         if overlaps[(claim[1]+i, claim[2]+j)] > 1:
            no_overlap = False
   if no_overlap:
      print('Part 2:', claim[0])
      break
