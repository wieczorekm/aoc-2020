with open('day5.in') as f:
    lines = [line.rstrip() for line in f]

all_ids = []

for s in lines:
    x = s.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
    id = int(x, 2)
    r = int(row, 2)
    c = int(column, 2)
    id = r * 8 + c
    all_ids.append(id)


all_ids = sorted(all_ids)

for i in range(len(all_ids)-1):
    if all_ids[i-1]+1 != all_ids[i]:
        print(all_ids[i-1], all_ids[i], all_ids[i+1])