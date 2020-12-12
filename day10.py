with open('day10.in') as f:
    lines = [line.rstrip() for line in f]

nums = []
for l in lines:
    nums.append(int(l))

nums.sort()

one = 0
two = 0
three = 0

for i in range(len(nums)-1):
    if nums[i+1] - nums[i] == 1:
        one += 1
    elif nums[i+1] - nums[i] == 2:
        two += 1
    elif nums[i+1] - nums[i] == 3:
        three += 1
    else:
        print(nums[i+1], i)
        assert False



nums.append(nums[-1] + 3)
nums.append(0)
nums.sort()

print(nums)

dic = {}

def rec(i, acc = 1):
    if i == len(nums) - 1:
        print("printing for " + str(nums[i]) + " " + str(acc))
        return acc

    if i in dic:
        return acc * dic[i]
    print("executing for i " + str(i))
    newacc = 0
    newacc += rec(i+1, acc)
    if i < len(nums) - 2 and nums[i+2] - nums[i] < 4:
        newacc += rec(i+2, acc)
    if i < len(nums) - 3 and nums[i+3] - nums[i] < 4:
        newacc += rec(i+3, acc)

    dic[i] = acc * newacc
    return acc * newacc


print(rec(0))
print(dic)
