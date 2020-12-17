with open('day16.in') as f:
# with open('day16.sample') as f:
    lines = [line.rstrip() for line in f]

params = {}

my_ticket = ""

other_tickets = []

mode = 0
for i in range(len(lines)):
    if not lines[i].strip():
        mode += 1
        i += 1
        continue
    if mode == 0:
        sp = lines[i].split(": ")
        ranges = sp[1].split(" or ")
        r1 = ranges[0].split("-")
        r2 = ranges[1].split("-")
        ri1 = (int(r1[0]), int(r1[1]))
        ri2 = (int(r2[0]), int(r2[1]))
        params[sp[0]] = (r1, r2)
    elif mode == 1:
        my_ticket = lines[i]
    elif mode == 2:
        if "nearby tickets:" in lines[i]:
            continue
        other_tickets.append(lines[i])
    else:
        assert False


err = 0
a = set()
b = set()
for o in other_tickets:
    nums = o.split(",")
    a.add(o)
    cnt = 0
    for n in nums:
        x = int(n)
        found = False
        for _, v in params.items():
            if int(v[0][0]) <= x <= int(v[0][1]) or int(v[1][0]) <= x <= int(v[1][1]):
                found = True
        if not found:
            cnt += 1

    if cnt > 0:
        b.add(o)
    elif cnt > len(params):
        assert False

c = a - b
c = sorted(c)

listDic = []
for l in c:
    d = []
    nums = l.split(",")
    for n in nums:
        s = set()
        x = int(n)
        for k, v in params.items():
            if int(v[0][0]) <= x <= int(v[0][1]) or int(v[1][0]) <= x <= int(v[1][1]):
                s.add(k)
        d.append(s)

    listDic.append(d)

merged = []
for j in range(len(listDic[0])):
    merged.append(listDic[0][j])
    if len(merged[j]) == 0:
        assert False

for i in range(1, len(listDic)):
    for j in range(len(listDic[0])):
        aa = listDic[i][j].intersection(merged[j])
        merged[j] = aa
        if len(merged[j]) == 0:
            assert False

mapping = {}

work = True
while work:
    work = False
    for i in range(20):
        if len(merged[i]) == 1:
            work = True
            elem = list(merged[i])[0]
            mapping[i] = elem
            for e in merged:
                try:
                    e.remove(elem)
                except Exception:
                    pass

res = 1
mt = my_ticket.split(",")
for k, v in mapping.items():
    if "departure" in v:
        res *= int(mt[k])

print(res)

