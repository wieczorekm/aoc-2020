inp = "586439172"

FILLING = 1_000_000
MOVES = 10_000_000

MAX = FILLING


class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.nextNode = None

DCT = {}

head = LinkedListNode(int(inp[0]))
DCT[int(inp[0])] = head

curr = LinkedListNode(int(inp[1]))
DCT[int(inp[1])] = curr
head.nextNode = curr
prev = head


for i in range(2, FILLING):
    if i < len(inp):
        tmp = LinkedListNode(int(inp[i]))
    else:
        tmp = LinkedListNode(i+1)

    DCT[tmp.val] = tmp
    prev.nextNode = curr
    prev = curr
    curr = tmp

prev.nextNode = curr
curr.nextNode = head


curr = head


x = head
for j in range(FILLING):
    if x.nextNode == None:
        assert False
    x = x.nextNode

printHelper = 0
for i in range(MOVES):
    printHelper += 1
    if printHelper % 1000 == 0:
        print("iter " + str(printHelper))
    currVal = curr.val
    one = curr.nextNode
    two = curr.nextNode.nextNode
    three = curr.nextNode.nextNode.nextNode
    curr.nextNode = three.nextNode
    if three.nextNode is None:
        assert False

    potentialDesc = currVal - 1
    if potentialDesc == 0:
        potentialDesc = MAX
    while potentialDesc in [0, one.val, two.val, three.val]:
        if potentialDesc <= 0:
            potentialDesc = MAX+1
        potentialDesc -= 1

    dest = DCT[potentialDesc]

    destNeighbor = dest.nextNode
    if destNeighbor is None:
        assert False

    dest.nextNode = one
    three.nextNode = destNeighbor

    curr = curr.nextNode
    if curr is None:
        assert False


it = curr
for i in range(FILLING):
    if it.val == 1:
        print("{} {} {}".format(it.val, it.nextNode.val, it.nextNode.nextNode.val))
        break
    it = it.nextNode

# for i in range(MOVES):
#     if i % 1000 == 0:
#         print("move {}".format(i))
#     idx = i
#     if prevCap != "":
#         prevCapIdx = -1
#         for j in range(len(INP)):
#             if INP[j] == prevCap:
#                 prevCapIdx = j
#                 break
#         assert prevCapIdx != -1
#         idx = prevCapIdx + 1
#     one = INP[(idx + 1) % len(INP)]
#     two = INP[(idx + 2) % len(INP)]
#     three = INP[(idx + 3) % len(INP)]
#     currentCap = INP[idx % len(INP)]
#     #print("current cap {}, three {} {} {} ".format(currentCap, one, two, three))
#     prevCap = currentCap
#     INP.remove(one)
#     INP.remove(two)
#     INP.remove(three)
#
#     potentialDesc = int(currentCap)-1
#
#     while True:
#         if potentialDesc in INP:
#             break
#         if potentialDesc <= 0 :
#             potentialDesc = MAX + 1
#         potentialDesc -= 1
#
#     destIdx = -1
#     for j in range(len(INP)):
#         if INP[j] == potentialDesc:
#             destIdx = j
#             break
#
#     assert destIdx != -1
#
#     INP.insert(destIdx+1, one)
#     INP.insert(destIdx+2, two)
#     INP.insert(destIdx+3, three)
#
#
# oneIdx = -1
# print(INP[0], INP[1], INP[2])
# for i in range(len(INP)):
#     if INP[i] == 1:
#         print(INP[i], INP[i+1], INP[i+2])
#         break