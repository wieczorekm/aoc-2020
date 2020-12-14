with open('day12.in') as f:
    lines = [line.rstrip() for line in f]


moves = []
for l in lines:
    moves.append((l[:1], int(l[1:])))

print(moves)

currx, curry = 0, 0

wayx, wayy = 10, 1

for m in moves:
    if m[0] == "N":
        wayy += m[1]
    if m[0] == "S":
        wayy -= m[1]
    if m[0] == "W":
        wayx -= m[1]
    if m[0] == "E":
        wayx += m[1]
    if m[0] == "F":
        currx += m[1]*wayx
        curry += m[1]*wayy
    if m[0] == "L" or m[0] == "R":
        if m[1] == 180:
            wayx *= -1
            wayy *= -1
        if (m[0] == "L" and m[1] == 90) or (m[0] == "R" and m[1] == 270):
            oldx = wayx
            oldy = wayy
            wayx = -oldy
            wayy = oldx
        if (m[0] == "R" and m[1] == 90) or (m[0] == "L" and m[1] == 270):
            oldx = wayx
            oldy = wayy
            wayx = oldy
            wayy = -oldx
    print(currx, curry, abs(currx)+abs(curry))


