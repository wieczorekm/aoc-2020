with open('day14.in') as f:
    lines = [line.rstrip() for line in f]

import re

d = {}
mask = ""
for l in lines:
    p = l.split(" = ")
    if p[0] == "mask":
        mask = p[1]
        print("mask: " + mask)
        continue

    idx = re.findall(r'\d+', p[0])[0]
    b = bin(int(p[1]))
    print(p[1], b)
    padded = "00000000000000000000000000000000000000000000000" + b[2:]
    print(padded)
    out = ""
    for i in range(len(mask)):
        padi = len(padded) - len(mask) + i
        if mask[i] == "X":
            out = out + padded[padi]
        else:
            out = out + mask[i]
    print("out "  + out)

    d[idx] = int(out, 2)

s = 0
for k, v in d.items():
    s += v

print(s)
