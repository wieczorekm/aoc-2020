with open('day13.in') as f:
    lines = [line.rstrip() for line in f]

timestamp = int(lines[0])

buses = lines[1].split(",")

m = 1
for i in range(len(buses)):
    if buses[i] != "x":
        print("x = -" + str(i) + " mod " + buses[i])
        m *= int(buses[i])


print(30858264669197331 % m)
