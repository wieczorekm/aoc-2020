with open('day11.in') as f:
    lines = [line.rstrip() for line in f]

orggrid = []
for i in range(len(lines)):
    orggrid.append([])
    for c in lines[i]:
        orggrid[i].append(c)


def iterate(grid):
    newGrid = []
    for i in range(len(lines)):
        newGrid.append([])
        for c in grid[i]:
            newGrid[i].append(c)


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count = 0
            ii = 1
            jj = 1
            while True:
                if not (i-ii >= 0 and j-jj >= 0):
                    break
                print("")
                print(ii, jj)
                print(i-ii, j-jj)
                v = grid[i-ii][j-jj]
                print(v)
                if v == '#':
                    count += 1
                    break
                if v == "L":
                    break
                ii += 1
                jj += 1

            ii = 1
            while True:
                if not (i-ii >= 0):
                    break
                v = grid[i-ii][j]
                if v == '#':
                    count += 1
                    break
                if v == "L":
                    break
                ii += 1

            ii = 1
            jj = 1
            while True:
                if not (i-ii >= 0 and j+jj < len(grid[0])):
                    break
                v = grid[i-ii][j+jj]
                if v == '#':
                    count += 1
                    break
                if v == "L":
                    break
                ii += 1
                jj += 1



            jj = 1
            while True:
                if not (j-jj >= 0):
                    break
                v = grid[i][j-jj]
                if v == '#':
                    count += 1
                    break
                if v == "L":
                    break
                jj += 1


            jj = 1
            while True:
                if not (j+jj < len(grid[0])):
                    break
                v = grid[i][j+jj]
                if v == '#':
                    count += 1
                    break
                if v == "L":
                    break
                jj += 1


            ii = 1
            jj = 1
            while True:
                if not (i + ii < len(grid) and j - jj >= 0):
                    break
                v = grid[i+ii][j-jj]
                if v == '#':
                    count += 1
                    break
                if v == "L":
                    break
                ii += 1
                jj += 1


            ii = 1
            while True:
                if not (i + ii < len(grid)):
                    break
                v = grid[i+ii][j]
                if v == '#':
                    count += 1
                    break
                if v == "L":
                    break
                ii += 1

            ii = 1
            jj = 1
            while True:
                if not (i + ii < len(grid) and j + jj < len(grid[0])):
                    break
                v = grid[i+ii][j+jj]
                if v == '#':
                    count += 1
                    break
                if v == "L":
                    break
                ii += 1
                jj += 1



            if grid[i][j] == "L" and count == 0:
                newGrid[i][j] = "#"
            if grid[i][j] == "#" and count >= 5:
                newGrid[i][j] = "L"



    return newGrid

def compare(n, o):
    for i in range(len(n)):
        for j in range(len(n[0])):
            if n[i][j] != o[i][j]:
                return False
    return True


def printP(g):
    for l in g:
        print("".join(l))
    print("")


old = orggrid
while True:
    new = iterate(old)
    printP(new)
    if compare(old, new):
        print("finished")
        cnt = 0
        for i in range(len(old)):
            for j in range(len(old[0])):
                if old[i][j] == "#":
                    cnt += 1
        print(cnt)

        raise Exception("end")

    old = new