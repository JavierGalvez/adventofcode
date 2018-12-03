from collections import defaultdict

input = []
overlaps = defaultdict(int)

for claim in open('input.txt'):
   claim = claim.replace('@', '').split()
   identifier = int(claim[0][1:])
   loff, toff = map(int, claim[1][:-1].split(','))
   width, height = map(int, claim[2].split('x'))
   input.append([identifier, loff, toff, width, height])

   for i in range(width):
      for j in range(height):
         overlaps[(loff+i, toff+j)] += 1

for claim in input:
   no_overlap = True
   for i in range(claim[3]):
      for j in range(claim[4]):
         if overlaps[(claim[1]+i, claim[2]+j)] > 1:
            no_overlap = False
   if no_overlap:
      print(claim[0])
      break
