from string import ascii_lowercase as alphabet

input = open('inputs/5.txt').read().replace('\n','')

def compare(a, b):
   return abs(ord('A') - ord('a')) == abs(ord(a) - ord(b))

def collapse(line):
   stack = []
   for c in line:
      if not stack:
         stack.append(c)
      else:
         if compare(c, stack[-1]):
            stack.pop()
         else:
            stack.append(c)
   return len(stack)

def remove_instances(text, c):
   return text.replace(c, '').replace(c.upper(), '')

print('Part 1:', collapse(input))
print('Part 2:', min(collapse(remove_instances(input, c)) for c in alphabet))
