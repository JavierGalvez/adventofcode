from collections import defaultdict
from string import ascii_uppercase as alphabet
import bisect

def read_input():
   tree = {}
   for l in alphabet:
      tree[l] = []
   for line in open('inputs/7.txt'):
      a, b = line.split()[1], line.split()[7]
      bisect.insort(tree[b], a)
   return tree

def assign_job(jobs):
   job, waitlist = min(jobs.items(), key=lambda x: len(x[1]))
   return job if not waitlist else None

def job_done(j, jobs):
   for k, v in jobs.items():
      if j in v:
         v.remove(j)

def order (data):
   order = ''
   while data:
      p = assign_job(data)
      del data[p]
      order += p
      job_done(p, data)
   return order

def get_time(c):
   return 60 + alphabet.index(c) + 1

def time (data, n):
   workers = []
   time = 0
   while data:
      for c in workers:
         if time == get_time(c[0]) + c[1]:
            workers.remove(c)
            job_done(c[0], data)
      for i in range(n - len(workers)):
         if data:
            p = assign_job(data)
            if p != None:
               del data[p]
               workers.append((p, time))
      time += 1

   time += get_time(workers[0][0]) - 1
   return time

print('Part 1:', order(read_input()))
print('Part 2:', time(read_input(), 5))
