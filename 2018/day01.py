from itertools import cycle

input = [int(line) for line in open('inputs/1.txt')]
print('Part 1:', sum(input))

ret = 0
seen = set()
for frequency in cycle(input):
   ret += frequency
   if ret in seen:
      break
   seen.add(ret)

print('Part 2:', ret)
