from collections import defaultdict
from math import prod

data = input()

# Parse data
fields, myticket, tickets = data.split("\n\n")

fields_ranges = dict()
for line in fields.split("\n"):
    name, ranges = line.split(": ")
    fields_ranges[name] = tuple(map(int, ranges.replace(" or ", "-").split("-")))
    
myticket = list(map(int, myticket.split("\n")[1].split(",")))
tickets = [ list(map(int, t.split(","))) for t in tickets.split("\n")[1:] ]

def check_range(x, r):
    return r[0] <= x <= r[1] or r[2] <= x <= r[3]

# Find invalid tickets
sum_invalid = 0
invalid_tickets = set()
for i, t in enumerate(tickets):
    for val in t:
        # Not valid for any field
        if not any(check_range(val, r) for r in fields_ranges.values()):
            sum_invalid += val
            invalid_tickets.add(i)

# Remove invalid tickets
for i, t in enumerate(sorted(invalid_tickets)):
    tickets.pop(t-i)

# Find valid columns for each field
valid_columns = defaultdict(list)
for name, r in fields_ranges.items():
    for i, column in enumerate(zip(*tickets)):
        if all(check_range(val, r) for val in column):
            valid_columns[name].append(i)

# Assign a column for each field
set_column = dict()
s = sorted(valid_columns.items(), key=lambda x: len(x[1]))
for field, columns in s:
    for c in columns:
        if c not in set_column.values():
            set_column[field] = c

print("Part 1: %d" % sum_invalid)
print("Part 2: %d" % prod([ myticket[col] for field, col in set_column.items() if "departure" in field ]))