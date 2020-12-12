with open('day12.in') as f:
    lines = [line.rstrip() for line in f]


moves = []
for l in lines:
    moves.append((l[:1], int(l[1:])))

print(moves)

currx, curry = 0, 0
delx, dely = 1, 0


for m in moves:
    if m[0] == "N":
        curry += m[1]
    if m[0] == "S":
        curry -= m[1]
    if m[0] == "W":
        currx -= m[1]
    if m[0] == "E":
        currx += m[1]
    if m[0] == "F":
        currx += m[1]*delx
        curry += m[1]*dely
    if m[0] == "L":
        if m[1] == 90:
            if delx == 0 and dely == 1:
                delx = -1
                dely = 0
            elif delx == 0 and dely == -1:
                delx = 1
                dely = 0
            elif delx == 1 and dely == 0:
                delx = 0
                dely = 1
            elif delx == -1 and dely == 0:
                delx = 0
                dely = -1
            else:
                assert False
        elif m[1] == 180:
            delx *= -1
            dely *= -1
        elif m[1] == 270:
            if delx == 0 and dely == 1:
                delx = 1
                dely = 0
            elif delx == 0 and dely == -1:
                delx = -1
                dely = 0
            elif delx == 1 and dely == 0:
                delx = 0
                dely = -1
            elif delx == -1 and dely == 0:
                delx = 0
                dely = 1
            else:
                assert False
        else:
            assert False
    if m[0] == "R":
        if m[1] == 90:
            if delx == 0 and dely == 1:
                delx = 1
                dely = 0
            elif delx == 0 and dely == -1:
                delx = -1
                dely = 0
            elif delx == 1 and dely == 0:
                delx = 0
                dely = -1
            elif delx == -1 and dely == 0:
                delx = 0
                dely = 1
            else:
                assert False
        elif m[1] == 180:
            delx *= -1
            dely *= -1
        elif m[1] == 270:
            if delx == 0 and dely == 1:
                delx = -1
                dely = 0
            elif delx == 0 and dely == -1:
                delx = 1
                dely = 0
            elif delx == 1 and dely == 0:
                delx = 0
                dely = 1
            elif delx == -1 and dely == 0:
                delx = 0
                dely = -1
            else:
                assert False
        else:
            assert False

    print(currx, curry, abs(currx)+abs(curry))


