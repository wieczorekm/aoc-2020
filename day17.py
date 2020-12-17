with open('day17.in') as f:
    lines = [line.rstrip() for line in f]

D = {}
D[0] = {}
for i, l1 in enumerate(lines):
    D[0][i] = {}
    for j, l2 in enumerate(l1):
        D[0][i][j] = l2

print(D)

import itertools
AA = [-1, 0, 1]
P = [p for p in itertools.product(AA, repeat=3)]
P.remove((0, 0, 0))

LIMIT = 6
curr = D
yy = len(D[0])
zz = len(D[0][0])
for iteration in range(LIMIT):
    print(iteration, len(curr), len(curr[0]), len(curr[0][0]))
    print(curr)
    new = {}
    for x in range(-iteration-2, iteration+6):
        for y in range(-iteration-1, yy+iteration+2):
            for z in range(-iteration-1, zz+iteration+2):
                aliveNeighbors = 0
                for p in P:
                    d_x, d_y, d_z = p
                    try:
                        val = curr[x+d_x][y+d_y][z+d_z]
                        if val == "#":
                            aliveNeighbors += 1
                        elif val != ".":
                            print(val)
                            assert False
                    except KeyError:
                        pass
                if x not in new:
                    new[x] = {}
                if y not in new[x]:
                    new[x][y] = {}

                try:
                    existing = curr[x][y][z]
                except KeyError:
                    existing = "."

                if existing == "#":
                    if 2 <= aliveNeighbors <= 3:
                        new[x][y][z] = "#"
                else:
                    if aliveNeighbors == 3:
                        new[x][y][z] = "#"
    curr = new


cnt = 0
for _, v1 in curr.items():
    for _, v2 in v1.items():
        for _, v3 in v2.items():
            if v3 == "#":
                cnt += 1

print(cnt)
