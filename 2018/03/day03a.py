from collections import defaultdict

overlaps = defaultdict(int)
for claim in open('input.txt'):
   claim = claim.replace('@','').split()
   loff, toff = map(int, claim[1][:-1].split(','))
   width, height = map(int, claim[2].split('x'))
   for i in range(width):
      for j in range(height):
         overlaps[(loff+i, toff+j)] += 1

ret = 0
for k, v in overlaps.items():
   if v > 1:
      ret += 1
print(ret)
