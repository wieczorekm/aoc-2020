with open('day8.in') as f:
    lines = [line.rstrip() for line in f]

global_instructions = []

for l in lines:
    x = l.split(" ")
    global_instructions.append((x[0], int(x[1])))

for i in range(len(global_instructions)):
    accumulator = 0
    idx = 0
    visited = set()
    instructions = global_instructions.copy()
    gop, gv = instructions[i]
    if gop == "acc":
        continue
    elif gop == "nop":
        instructions[i] = ("jmp", gv)
    elif gop == "jmp":
        instructions[i] = ("nop", gv)
    else:
        assert False
    print(i)
    while True:
        print(accumulator)
        op, v = instructions[idx]
        visited.add(idx)
        if op == "nop":
            idx += 1
        elif op == "acc":
            accumulator += v
            idx += 1
        elif op == "jmp":
            idx += v
        else:
            assert False
        if idx > len(instructions):
            print("finished")
            print(accumulator)
            break
        if idx in visited:
            print(accumulator)
            break