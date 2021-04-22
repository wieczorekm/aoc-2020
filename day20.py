# with open('day20.sample') as f:
#     validCoords = [['1951', '2311', '3079'], ['2729', '1427', '2473'], ['2971', '1489', '1171']]
#     validRotations = [[(2, True), (2, True), (0, False)], [(2, True), (2, True), (1, True)], [(2, True), (2, True), (0, True)]]
#     lines = [line.rstrip() for line in f]

with open('day20.in') as f:
    validCoords = [['1723', '3881', '3433', '3617', '3541', '1097', '3203', '2843', '3163', '2657', '2687', '2221'], ['1697', '1453', '2591', '2879', '3217', '1933', '1579', '2381', '3469', '3793', '3169', '2243'], ['1721', '2273', '1669', '3467', '3361', '2003', '2713', '1973', '1489', '1459', '3989', '1223'], ['2459', '3041', '1759', '2531', '3343', '1153', '3253', '1657', '3643', '2857', '2549', '1777'], ['3923', '2029', '2683', '3391', '3533', '3823', '3851', '2897', '1543', '3917', '3517', '1297'], ['2039', '3803', '2357', '1861', '1229', '3191', '2207', '3209', '3221', '2927', '3331', '1063'], ['2539', '3089', '2137', '2749', '1663', '3779', '3797', '1279', '2063', '3769', '1483', '1249'], ['1187', '2633', '3889', '1117', '2711', '1867', '3119', '2081', '3929', '2767', '1259', '1549'], ['1787', '1171', '1033', '2203', '2237', '1583', '1801', '3463', '3373', '3413', '1621', '1811'], ['1747', '1181', '2729', '2143', '1741', '2671', '1123', '3623', '3329', '2969', '1301', '3527'], ['2087', '1013', '2293', '1523', '1429', '1951', '3919', '3323', '3697', '1319', '1627', '1907'], ['2287', '2129', '2833', '1487', '3299', '2659', '3271', '3511', '3943', '2999', '3581', '1511']]
    validRotations = [[(2, True), (0, False), (2, True), (3, False), (0, True), (0, True), (2, True), (0, False), (2, False), (0, False), (3, False), (2, False)], [(1, False), (3, False), (2, True), (0, False), (0, True), (2, True), (1, True), (3, False), (2, True), (3, False), (2, False), (1, False)], [(2, False), (3, False), (2, True), (2, False), (2, False), (1, True), (3, False), (2, False), (2, False), (1, False), (1, True), (3, False)], [(2, True), (3, False), (1, True), (3, False), (1, False), (3, False), (1, True), (1, False), (3, False), (0, False), (2, False), (0, True)], [(1, False), (1, False), (2, True), (2, False), (3, False), (3, False), (0, False), (0, False), (2, False), (1, True), (3, False), (3, False)], [(1, False), (1, True), (2, True), (0, True), (0, False), (1, True), (3, False), (0, True), (1, True), (0, False), (1, True), (0, False)], [(0, False), (2, True), (3, False), (0, False), (0, False), (0, True), (0, True), (0, True), (1, False), (3, False), (3, False), (1, False)], [(2, True), (2, True), (1, False), (0, True), (2, True), (1, False), (1, True), (0, True), (1, True), (1, True), (1, True), (2, True)], [(1, False), (0, True), (0, True), (1, False), (0, True), (1, False), (0, True), (0, False), (1, False), (2, False), (0, False), (2, False)], [(0, False), (1, True), (2, True), (3, False), (1, False), (0, True), (2, False), (1, False), (1, True), (2, False), (3, False), (2, False)], [(0, False), (2, True), (1, True), (2, True), (2, True), (0, False), (0, False), (2, False), (1, False), (2, True), (1, False), (3, False)], [(0, False), (0, False), (2, True), (2, True), (3, False), (2, True), (0, True), (1, True), (2, False), (2, True), (1, True), (2, False)]]
    lines = [line.rstrip() for line in f]

import re

curr = re.findall(r"\d+", lines[0])[0]

d = {}
d[curr] = []
for i in range(1, len(lines)):
    if not lines[i].strip():
        i+=1
        print(lines[i])
        curr = re.findall(r"\d+", lines[i])[0]
        print(curr)
        d[curr] = []
    else:
        if "Tile" not in lines[i]:
            d[curr].append(lines[i])

borders = {}
for k,v in d.items():
    up = v[0]
    down = v[-1]
    left = []
    for i in range(len(v[0])):
        left.append(v[i][0])
    right = []
    for i in range(len(v[0])):
        right.append(v[i][-1])

    left = "".join(left)
    right = "".join(right)

    borders[k] = (up, down, left, right)

print(borders)

def rotateLeft(corners):
    o_up, o_down, o_left, o_right = corners
    up = o_right
    down = o_left
    left = o_up[::-1]
    right = o_down[::-1]
    return (up, down, left, right)

def flip(corners):
    o_up, o_down, o_left, o_right = corners
    up = o_up[::-1]
    down = o_down[::-1]
    left = o_right
    right = o_left
    return (up, down, left, right)

for i in range(100):
    print(i, len(d))
    if i*i == len(d):
        SIDE_LEN = i
        break

#print(SIDE_LEN)
r = rotateLeft(("LHJI", "ABCD", "MNOP", "HGFE"))
#print(r)

M = []
for xxx in range(SIDE_LEN):
    M.append([])
    for _ in range(SIDE_LEN):
        M[xxx].append(None)

IDS = []
for xxx in range(SIDE_LEN):
    IDS.append([])
    for _ in range(SIDE_LEN):
        IDS[xxx].append(None)

ORIENTATION = []
for xxx in range(SIDE_LEN):
    ORIENTATION.append([])
    for _ in range(SIDE_LEN):
        ORIENTATION[xxx].append(None)

def validateAll():
    #print("validating")
    for i in range(SIDE_LEN):
        for j in range(SIDE_LEN):
            if M[i][j] is not None:
                if i > 0:
                    if M[i-1][j] is None:
                        pass
                    elif M[i][j][0] != M[i-1][j][1]:
                        #print("validation A")
                        return False
                if i < SIDE_LEN - 1:
                    if M[i+1][j] is None:
                        pass
                    elif M[i][j][1] != M[i+1][j][0]:
                        #print("validation B")
                        return False
                if j > 0:
                    if M[i][j-1] is None:
                        pass
                    elif M[i][j][2] != M[i][j-1][3]:
                        #print("validation C")
                        return False
                if j < SIDE_LEN - 1:
                    if M[i][j+1] is None:
                        pass
                    elif M[i][j][3] != M[i][j+1][2]:
                        #print("validation D", M[i][j][3], M[i][j+1][2])
                        return False
    return True

used = set()
#print(M)


def rec(idx):
    valid = validateAll()
    d_i = idx//SIDE_LEN
    d_j = idx%SIDE_LEN

    log_i = (idx-1)//SIDE_LEN
    log_j = (idx-1)%SIDE_LEN
    if not valid:
        return False

    if idx == SIDE_LEN*SIDE_LEN:
        #print(M)
        print(IDS)
        print(int(IDS[0][0])*int(IDS[0][-1])*int(IDS[-1][0])*int(IDS[-1][-1]))
        #print("found!!!!!!!!!!!!!!!!!")
        assert False

    #print(d_i, d_j)
    #print("[depth: {}] - starting loop".format(idx))
    #print(borders.items())
    for k, v in borders.items():
        if idx == 0:
            print("depth 0 - calculating for " + k)
        #print("[depth: {}] - next iter for k=[{}]".format(idx, k))

        if k not in used:
            #print("[depth: {}] - k [{}] not used yet".format(idx, k))
            #print(borders)

            used.add(k)
            IDS[d_i][d_j] = k

            M[d_i][d_j] = v
            ORIENTATION[d_i][d_j] = (0, False)
            _ = rec(idx+1)
            M[d_i][d_j] = None
            f = flip(v)
            M[d_i][d_j] = f
            ORIENTATION[d_i][d_j] = (0, True)
            _ = rec(idx+1)
            M[d_i][d_j] = None

            v1 = rotateLeft(v)
            M[d_i][d_j] = v1
            ORIENTATION[d_i][d_j] = (1, False)
            _ = rec(idx+1)
            M[d_i][d_j] = None
            f1 = flip(v1)
            M[d_i][d_j] = f1
            ORIENTATION[d_i][d_j] = (1, True)
            _ = rec(idx+1)
            M[d_i][d_j] = None

            v2 = rotateLeft(v1)
            M[d_i][d_j] = v2
            ORIENTATION[d_i][d_j] = (2, False)
            _ = rec(idx+1)
            M[d_i][d_j] = None
            f2 = flip(v2)
            M[d_i][d_j] = f2
            ORIENTATION[d_i][d_j] = (2, True)
            _ = rec(idx+1)
            M[d_i][d_j] = None

            v3 = rotateLeft(v2)
            M[d_i][d_j] = v3
            ORIENTATION[d_i][d_j] = (3, False)
            _ = rec(idx+1)
            M[d_i][d_j] = None
            f3 = flip(v3)
            M[d_i][d_j] = f3
            ORIENTATION[d_i][d_j] = (3, True)
            _ = rec(idx+1)
            M[d_i][d_j] = None

            IDS[d_i][d_j] = None
            used.remove(k)
        # else:
            #print("[depth: {}] - key [{}] was already used".format(idx, k))

    #print(M)
    return False
# try:
#     x = rec(0)
# except AssertionError:
#     pass
# print(rec)
# print(M)

print(ORIENTATION)

def flipGrid(grid):
    r = []
    for i in grid:
        r.append(i[::-1])
    return r

def rotLeftGrid(grid):
    r = []
    for i in range(len(grid)):
        r.append([])
        for j in range(len(grid[i])):
            r[i].append('')

    A = list(list(x)[::-1] for x in zip(*grid))
    A = list(list(x)[::-1] for x in zip(*A))
    A = list(list(x)[::-1] for x in zip(*A))
    B = []
    for i in A:
        B.append("".join(i))

    return B


X3 = [
    'ABC',
    'EGH',
    'KAS'
]

X4 = [
    '1234X',
    '5678X',
    '90ABX',
    'CDEFX',
    'TYYYY',
]

def removeBorders(Z):
    Y = []
    for k in range(1, len(Z)-1):
        Y.append(Z[k][1:len(Z[k])-1])
    return Y

MM = []
for i in range(SIDE_LEN):
    MM.append([])
    for j in range(SIDE_LEN):
        MM[i].append(None)

for i in range(len(validCoords)):
    for j in range(len(validCoords[0])):
        X = d[validCoords[i][j]]
        Z = X
        print(validRotations[i][j])
        for k in range(validRotations[i][j][0]):
            Z = rotLeftGrid(Z)
        if validRotations[i][j][1] == True:
            print("fliping for ", i, j)
            Z = flipGrid(Z)
        MM[i][j] = removeBorders(Z)


final = []
for i in range(len(MM)):
    lines = []
    for j in range(len(MM[0][0])):
        lines.append("")
    for k in range(len(MM[0][0])):
        for j in range(len(MM[0])):
            lines[k] += MM[i][j][k]
    for l in lines:
        final.append(l)

for l in final:
    print(l)

PATTERN = []
PATTERN.append("                  # ")
PATTERN.append("#    ##    ##    ###")
PATTERN.append(" #  #  #  #  #  #   ")


COMBINATIONS = []


SEA_MONSTERS = 0

for i in range(4):
    # not flipped
    A = final
    for rots in range(i):
        A = rotLeftGrid(A)
    COMBINATIONS.append(A)
    # flipped
    B = flipGrid(A)
    COMBINATIONS.append(B)

for comb in COMBINATIONS:
    for i in range(len(comb)-len(PATTERN)):
        for j in range(len(comb[0])-len(PATTERN[0])):
            monster = True
            for pattern_i in range(len(PATTERN)):
                for pattern_j in range(len(PATTERN[0])):
                    if PATTERN[pattern_i][pattern_j] == "#":
                        if comb[i+pattern_i][j+pattern_j] != "#":
                            monster = False
            if monster:
                print("found sea monster ", i, j )
                SEA_MONSTERS += 1



XCOUNT = 0
for l in final:
    for c in l:
        if c == "#":
            XCOUNT += 1

print("XCOUNT " + str(XCOUNT))
print("SEA MONSTERS COUNT " + str(SEA_MONSTERS))
print("RESULT " + str(XCOUNT - 15*SEA_MONSTERS))



