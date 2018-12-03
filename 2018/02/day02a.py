from collections import Counter
input = [line for line in open('input.txt')]
twice, threeTimes = 0, 0
for row in input:
   count = {n for i, n in Counter(row).most_common()}
   if 2 in count:
      twice += 1
   if 3 in count:
      threeTimes += 1
print(twice * threeTimes)
