data = list(map(int, open('inputs/8.txt').read().split()))

def helper(data):
	num_branches, num_metadata = data.pop(0), data.pop(0)
	sum_metadata = 0
	values = []

	for _ in range(num_branches):
		sum_branch, data, val = helper(data)
		sum_metadata += sum_branch
		values.append(val)
	
	sum_metadata += sum(data[:num_metadata])

	if num_branches == 0:
		return sum_metadata, data[num_metadata:], sum_metadata
	else:
		return sum_metadata, data[num_metadata:], sum(values[k-1] for k in data[:num_metadata] if k-1 < num_branches and k > 0)
	
sum_metadatas, _, root_value = helper(data)
print('Part 1:', sum_metadatas)
print('Part 2:', root_value)
