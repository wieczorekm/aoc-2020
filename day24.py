with open('day24.in') as f:
    lines = [line.rstrip() for line in f]

instructions = []

for l in lines:
    line_instructions = []
    i = 0
    while i < len(l):
        if "e" == l[i] or "w" == l[i]:
            line_instructions.append(l[i])
        elif l[i:i+2] in ["se", "sw", "ne", "nw"]:
            line_instructions.append(l[i:i+2])
            i += 1
        else:
            assert False
        i += 1
    instructions.append(line_instructions)

flipped = set()

for line_instructions in instructions:
    print(line_instructions)
    x, y = 0, 0
    for i in line_instructions:
        if i == "e":
            x += 2
        elif i == "w":
            x -= 2
        elif i == "se":
            x += 1
            y -= 1
        elif i == "sw":
            x -= 1
            y -= 1
        elif i == "ne":
            x += 1
            y += 1
        elif i == "nw":
            x -= 1
            y += 1
        else:
            assert False
    if (x, y) in flipped:
        flipped.remove((x, y))
    else:
        flipped.add((x, y))

print(flipped)

print(len(flipped))

prev = flipped.copy()


def blackNeighbors(x, y):
    count = 0
    if (x-2, y) in prev:
        count += 1

    if (x+2, y) in prev:
        count += 1

    if (x+1, y+1) in prev:
        count += 1

    if (x+1, y-1) in prev:
        count += 1

    if (x-1, y+1) in prev:
        count += 1

    if (x-1, y-1) in prev:
        count += 1

    return count


DAYS = 100+1


for day in range(DAYS):
    print("day {}: {}".format(day, len(prev)))
    curr = set()
    for black in prev:
        xx, yy = black
        cnt = blackNeighbors(xx, yy)
        if cnt == 1 or cnt == 2:
            curr.add((xx, yy))

        if (xx-2, yy) not in prev and blackNeighbors(xx-2, yy) == 2:
            curr.add((xx-2, yy))

        if (xx+2, yy) not in prev and blackNeighbors(xx+2, yy) == 2:
            curr.add((xx+2, yy))

        if (xx+1, yy+1) not in prev and blackNeighbors(xx+1, yy+1) == 2:
            curr.add((xx+1, yy+1))

        if (xx+1, yy-1) not in prev and blackNeighbors(xx+1, yy-1) == 2:
            curr.add((xx+1, yy-1))

        if (xx-1, yy+1) not in prev and blackNeighbors(xx-1, yy+1) == 2:
            curr.add((xx-1, yy+1))

        if (xx-1, yy-1) not in prev and blackNeighbors(xx-1, yy-1) == 2:
            curr.add((xx-1, yy-1))

    prev = curr

