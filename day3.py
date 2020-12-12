with open('day3.in') as f:
    lines = [line.rstrip() for line in f]


trees = 0

for i in range(len(lines)):
    singleLineLen = len(lines[i])
    chr = lines[i][3*i % singleLineLen]
    if chr == '#':
        trees += 1

trees2 = 0

for i in range(len(lines)):
    singleLineLen = len(lines[i])
    chr = lines[i][i % singleLineLen]
    if chr == '#':
        trees2 += 1


trees3 = 0

for i in range(len(lines)):
    singleLineLen = len(lines[i])
    chr = lines[i][5*i % singleLineLen]
    if chr == '#':
        trees3 += 1


trees4 = 0

for i in range(len(lines)):
    singleLineLen = len(lines[i])
    chr = lines[i][7*i % singleLineLen]
    if chr == '#':
        trees4 += 1


trees5 = 0

for i in range(len(lines)):
    j = 2*i
    if j >= len(lines):
        break
    singleLineLen = len(lines[i])
    chr = lines[j][i % singleLineLen]
    if chr == '#':
        trees5 += 1

print(trees*trees2*trees3*trees4*trees5)