with open('day6.in') as f:
    lines = [line.rstrip() for line in f]

groups = []

curr = []

for l in lines:
    if l == "":
        groups.append(curr)
        curr = []
    else:
        curr.append(l)

groups.append(curr)

count = 0

for g in groups:
    m = {}
    for l in g:
        distinct = set()
        for letter in l:
            if letter in distinct:
                continue
            if letter in m:
                m[letter] = m[letter] + 1
            else:
                m[letter] = 1
            distinct.add(letter)
    print(m)
    for k, v in m.items():
        if v == len(g):
            print(k, v)
            count += 1


print(count)