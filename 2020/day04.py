data = input()
data = data.split("\n\n")

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valids = [ p for p in data if -1 not in list(map(p.find, fields))]

valid = 0
for p in valids:
    fields = dict([x.split(":") for x in p.replace("\n", " ").split(" ")])
    
    byr = int(fields["byr"]) >= 1920 and int(fields["byr"]) <= 2002 
    iyr = int(fields["iyr"]) >= 2010 and int(fields["iyr"]) <= 2020
    eyr = int(fields["eyr"]) >= 2020 and int(fields["eyr"]) <= 2030
    hgt = (fields["hgt"][-2:] == "cm" and (int(fields["hgt"][:-2]) >= 150 and int(fields["hgt"][:-2]) <= 193)) or \
          (fields["hgt"][-2:] == "in" and (int(fields["hgt"][:-2]) >= 59 and int(fields["hgt"][:-2]) <= 76))
    hcl = fields["hcl"][0] == '#' and False not in [x in "0123456789abcdef" for x in fields["hcl"][1:]] 
    ecl = fields["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid = len(fields["pid"]) == 9 and fields["pid"].isdigit()
    
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid += 1
        
print("Part 1: %d" % len(valids))
print("Part 2: %d" % valid)