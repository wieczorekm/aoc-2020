with open('day2.in') as f:
    lines = [line.rstrip() for line in f]
from operator import xor

valid = 0
for l in lines:
    x = l.split(" ")
    f, t = x[0].split('-')
    frm = int(f)
    to = int(t)
    chr = x[1][0]
    psswrd = x[2]
    if xor(psswrd[frm-1] == chr, psswrd[to-1] == chr):
        valid += 1

print(valid)