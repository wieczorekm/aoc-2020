with open('day22.in') as f:
    lines = [line.rstrip() for line in f]

import re

GLOBAL = [1]

currentPlayer = -1

D = {}
for l in lines:
    if not l.strip():
        continue
    elif "Player" in l:
        currentPlayer = re.findall(r"\d", l)[0]
        D[currentPlayer] = []
    else:
        D[currentPlayer].append(int(l))

print(D)

first = D['1']
second = D['2']

def calcScore(x):
    score = 0
    for i in range(len(x)):
        score += x[i]*(len(x)-i)
    return score


def play(left, right, depth = 1):
    prevStates = set()
    print("Game " + str(GLOBAL[0]) + " depth " + str(depth))
    GLOBAL[0] += 1
    while True:
        if len(left) == 0:
            if len(right) == 2*len(D['1']):
               print(calcScore(right))
            return "right"
        if len(right) == 0:
            if len(left) == 2*len(D['1']):
                print(calcScore(right))
            return "left"
        if str((left, right)) in prevStates:
            return "left"
        prevStates.add(str((left, right)))
        fCard = left[0]
        sCard = right[0]
        left = left[1:]
        right = right[1:]

        if len(left) >= fCard and len(right) >= sCard:
            #print("entering combat, len left {}, len right {}, fcard {}, scard {}".format(len(left), len(right), fCard, sCard))
            lCopy = left.copy()[0:fCard]
            rCopy = right.copy()[0:sCard]
            ret = play(lCopy, rCopy, depth+1)
            if ret == "right":
                right.append(sCard)
                right.append(fCard)
            elif ret == "left":
                left.append(fCard)
                left.append(sCard)
            else:
                assert False

        elif fCard > sCard:
            left.append(fCard)
            left.append(sCard)
        elif sCard > fCard:
            right.append(sCard)
            right.append(fCard)
        else:
            assert False


play(first, second)
print("")
print("first")
print(first)
print("second")
print(second)