with open('day14.in') as f:
    lines = [line.rstrip() for line in f]

import re


def rec(s, arr):
    if s is None or s == "":
        return arr
    if s[:1] == "1" or s[:1] == "0":
        for i in range(len(arr)):
            arr[i] = arr[i] + s[:1]
    else:
        for i in range(len(arr)):
            a = arr[i]
            arr[i] = a + "0"
            arr.append(a + "1")
    return rec(s[1:], arr)

d = {}
mask = ""
for l in lines:
    p = l.split(" = ")
    if p[0] == "mask":
        mask = p[1]
        print("mask: " + mask)
        continue

    idx = re.findall(r'\d+', p[0])[0]
    b = bin(int(idx))
    padded = "00000000000000000000000000000000000000000000000" + b[2:]
    out = ""

    for i in range(len(mask)):
        padi = len(padded) - len(mask) + i
        if mask[i] == "0":
            out = out + padded[padi]
        else:
            out = out + mask[i]
    print("out "  + out)
    a = rec(out, [""])
    for x in a:
        d[x] = int(p[1])

s = 0
for k,v in d.items():
    s+=v
print(s)

