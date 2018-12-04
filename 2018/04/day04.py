from collections import defaultdict

input = [line.replace('\n','') for line in open('input.txt')]
input.sort()

def get_time(e):
   return int(e.split('] ')[0][15:])

hours_asleep = defaultdict(int)
total_hours = defaultdict(int)
guard = -1
for i, line in enumerate(input):
   if 'Guard' in line:
     guard = int(line.split()[3][1:])
   elif 'asleep' in line:
      for k in range(get_time(line), get_time(input[i+1])):
         hours_asleep[(guard, k)] += 1
         total_hours[guard] += 1

guard, _ = max(total_hours.items(), key=lambda x: x[1])
_, minute = max(hours_asleep.items(), key=lambda x: x[1] if x[0][0] == guard else -1)[0]
print('Part 1: ', guard * minute)

guard, minute = max(hours_asleep.items(), key=lambda x: x[1])[0]
print('Part 2: ', guard * minute)
