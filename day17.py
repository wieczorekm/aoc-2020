with open('day17.in') as f:
    lines = [line.rstrip() for line in f]

D = {}
D[0] = {}
D[0][0] = {}
for i, l1 in enumerate(lines):
    D[0][0][i] = {}
    for j, l2 in enumerate(l1):
        D[0][0][i][j] = l2

print(D)

import itertools
AA = [-1, 0, 1]
P = [p for p in itertools.product(AA, repeat=4)]
P.remove((0, 0, 0, 0))

LIMIT = 6
curr = D
yy = len(D[0][0])
zz = len(D[0][0][0])
for iteration in range(LIMIT):
    new = {}
    for w in range(-iteration-1, iteration+2):
        for x in range(-iteration-1, iteration+2):
            for y in range(-iteration-1, yy+iteration+2):
                for z in range(-iteration-1, zz+iteration+2):
                    aliveNeighbors = 0
                    for p in P:
                        d_x, d_y, d_z, d_w = p
                        try:
                            val = curr[w+d_w][x+d_x][y+d_y][z+d_z]
                            if val == "#":
                                aliveNeighbors += 1
                            elif val != ".":
                                print(val)
                                assert False
                        except KeyError:
                            pass
                    if w not in new:
                        new[w] = {}
                    if x not in new[w]:
                        new[w][x] = {}
                    if y not in new[w][x]:
                        new[w][x][y] = {}

                    try:
                        existing = curr[w][x][y][z]
                    except KeyError:
                        existing = "."

                    if existing == "#":
                        if 2 <= aliveNeighbors <= 3:
                            new[w][x][y][z] = "#"
                    else:
                        if aliveNeighbors == 3:
                            new[w][x][y][z] = "#"
    curr = new


cnt = 0
for _, v1 in curr.items():
    for _, v2 in v1.items():
        for _, v3 in v2.items():
            for _, v4 in v3.items():
                if v4 == "#":
                    cnt += 1

print(cnt)
