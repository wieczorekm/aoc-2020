with open('day15.in') as f:
    lines = [line.rstrip() for line in f]

nums = lines[0].split(",")

arr = []
d = {}

j = 0
for i in range(30000000):
    if i % 300000 == 0:
        j += 1
        print(str(j) + " %")
    if i < len(nums):
        arr.append(int(nums[i]))
        if nums[i] not in d:
            d[int(nums[i])] = [i]
        else:
            d[int(nums[i])].append(i)
    else:
        prev = arr[i-1]
        if len(d[prev]) == 1:
            arr.append(0)
            if 0 not in d:
                d[0] = [i]
            else:
                d[0].append(i)
        elif len(d[prev]) > 1:
            diff = d[prev][-1] - d[prev][-2]
            arr.append(diff)
            if diff not in d:
                d[diff] = [i]
            else:
                d[diff].append(i)
        else:
            assert False
print(arr[30000000-1])