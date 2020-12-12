with open('day7.in') as f:
    lines = [line.rstrip() for line in f]
import re

dict = {}
for line in lines:
    l = line.split("contain")
    left = l[0]
    leftColor = left.split(" bags")[0]
    if "no other bags" in l[1]:
        dict[leftColor] = {}
        continue
    right = l[1].split(",")
    rightMap = {}
    for r in right:
        m = re.search(r"\d+ .+ bag", r).group()
        m = m[:len(m)-4]
        num = int(m[:1])
        color = m[2:]
        rightMap[color] = num
    dict[leftColor] = rightMap

all = set()
curr = set()
next = set()

for c in dict.keys():
    for c2 in dict[c]:
        if c2 == "shiny gold":
            curr.add(c)

while len(curr) != 0:
    for c in dict.keys():
        for c2 in dict[c]:
            if c2 in curr and c2 not in all:
                next.add(c)

    for a in curr:
        all.add(a)

    curr = next
    next = set()

print(len(all))


def calc(i):
    print("")
    print("calculating for " + i)
    if len(dict[i]) == 0:
        print(i + " empty, result is 1")
        return 1
    else:
        sum = 0
        for k, v in dict[i].items():
            res = v * calc(k)
            sum += res
        print(i + " result is " + str(sum))
        return sum + 1

print(calc("shiny gold") - 1)
