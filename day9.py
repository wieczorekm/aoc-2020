with open('day9.in') as f:
    lines = [line.rstrip() for line in f]

nums = []
for l in lines:
    nums.append(int(l))

def sums(i):
    res = []
    for j in range(i-25, i-1):
        for k in range(j+1, i):
            res.append(nums[j] + nums[k])
    return res

res = 0
idx = 0
for i in range(25, len(nums)):
    if nums[i] not in sums(i):
        res = nums[i]
        idx = i
        break

print(res, idx)

# for j in range(0, idx-1):
#     for k in range(j+1, idx):
#         sum = 0
#         for g in range(j, k):
#             sum += nums[g]
#         if sum == res:
#             print("found")
#             print(j, k)

a = []
for g in range(396, 413):
    a.append(nums[g])

a.sort()

print(a)
print(a[0]+a[-1])
