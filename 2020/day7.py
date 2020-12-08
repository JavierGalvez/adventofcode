data = input()

bags = dict()
for line in data.split("\n"):
    line = line.replace("bags", "").replace("bag", "")[:-1]
    bag, contains = line.split("contain")
    bags[bag.strip()] = [x.split(" ", 1) for x in map(str.strip, contains.split(","))]

contain_shiny = set()
checking = ["shiny gold"]
while checking:
    checking_next = []
    for b, contain in bags.items():
        if b not in contain_shiny and any(c[1] == v for c in contain for v in checking):
            checking_next.append(b)
            contain_shiny.add(b)
    checking = checking_next


def part2(bags, color):
    return sum(int(n) + int(n) * part2(bags, current) for n, current in bags[color] if n != "no")

print("Part 1: %d" % len(contain_shiny))
print("Part 2: %d" % part2(bags, "shiny gold"))
