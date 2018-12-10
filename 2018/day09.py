from collections import defaultdict
from collections import deque
from re import findall

data = open('inputs/9.txt').read().split()

def play(player, n):
	scores = defaultdict(int)
	marbles = deque([0])
	for k in range(1, n+1):
		if k % 23 == 0:
			marbles.rotate(-7)
			scores[k%players] += marbles.pop() + k
		else:
			marbles.rotate(2)
			marbles.append(k)
	return max(scores.values())

players, marbles = map(int, findall('\d+', open('inputs/9.txt').read()))
print('Part 1:', play(players, marbles))
print('Part 2:', play(players, marbles*100))
