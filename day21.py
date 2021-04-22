with open('day21.in') as f:
# with open('day21.sample') as f:
    lines = [line.rstrip() for line in f]

ALL = []

for l in lines:
    foods = l.split(" (")[0].split(" ")
    x = l.split("contains ")[1]
    allegens = x[0:len(x)-1].split(", ")
    ALL.append((foods, allegens))

print(ALL)

MAPPING = {}
for l in ALL:
    for al in l[1]:
        if al not in MAPPING:
            MAPPING[al] = {}
        for food in l[0]:
            if food not in MAPPING[al]:
                MAPPING[al][food] = 1
            else:
                MAPPING[al][food] += 1

print("mapping")
for k, v in MAPPING.items():
    print(k, v)

FINAL_MAPPING = {}

while True:
    print("found " + str(len(FINAL_MAPPING)))
    for k, v in MAPPING.items():
        maxVal = 0
        for k1, v1 in v.items():
            maxVal = maxVal if maxVal > v1 else v1
        maxFoods = set()
        for k1, v1 in v.items():
            if maxVal == v1:
                maxFoods.add(k1)
        alreadyFound = set(FINAL_MAPPING.keys())
        candidates = maxFoods - alreadyFound
        if len(candidates) == 1:
            FINAL_MAPPING[list(candidates)[0]] = k

    if len(FINAL_MAPPING.keys()) == len(MAPPING.keys()):
        break

print(FINAL_MAPPING)
cnt = 0

for a in ALL:
    for l in a[0]:
        if l not in FINAL_MAPPING.keys():
            cnt += 1

print(cnt)

# mxmxvkd -> dairy
# sqjhc -> fish
# fvjkl -> soy

#lmxt,rggkbpj,mxf,nmtzlj,dlkxsxg,fvqg,gpxmf,dxzq

x = dict(sorted(FINAL_MAPPING.items(), key=lambda item: item[1]))
print(",".join(x.keys()))
