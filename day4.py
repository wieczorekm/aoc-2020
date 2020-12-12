with open('day4.in') as f:
    lines = [line.rstrip() for line in f]

passports = []

d = {}
for l in lines:
    if l == "":
        passports.append(d)
        d = {}
    else:
        for s in l.split(" "):
            print(s)
            k = s.split(":")
            d[k[0]] = k[1]

passports.append(d)


req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

cnt = 0
for p in passports:
    valid = True
    for r in req:
        if r not in p:
            valid = False
            break
    if not valid:
        continue
    if not (len(p["byr"]) == 4 and "1920" <= p["byr"] <= "2002"):
        valid = False
    if not (len(p["iyr"]) == 4 and "2010" <= p["iyr"] <= "2020"):
        valid = False
    if not (len(p["eyr"]) == 4 and "2020" <= p["eyr"] <= "2030"):
        valid = False
    hgt = p["hgt"]
    if hgt[-2:] == "cm":
        h = hgt[:len(hgt)-2]
        if not (len(h) == 3 and "150" <= h <= "193"):
            valid = False
    elif hgt[-2:] == "in":
        h = hgt[:len(hgt)-2]
        if not (len(h) == 2 and "59" <= h <= "76"):
            valid = False
    else:
        valid = False

    hcl = p["hcl"]
    if not (len(hcl) == 7 and hcl[0] == "#"):
        valid = False
    else:
        for i in range(1, 7):
            if not ("0" <= hcl[i] <= "9" or "a" <= hcl[i] <= "f" ):
                valid = False

    if not (p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] ):
        valid = False

    if not (len(p["pid"]) == 9 and "0" <= p["pid"] <= "999999999"):
        valid = False



    if valid:
        cnt += 1

print(cnt)
