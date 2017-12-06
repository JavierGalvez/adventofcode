from math import sqrt

# This only works if val is in the first column or in the last row (val > int(sqrt(val))**2)

val = 277678
pos = val - int(sqrt(val))**2

print(abs(int(sqrt(val)) / 2 - int(sqrt(val))) + abs(int(sqrt(val)) / 2 - (pos - int(sqrt(val)))) - 1)
