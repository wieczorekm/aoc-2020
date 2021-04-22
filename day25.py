
D = {}
def transferSubjectNumber(subjectNumber, loopSize):
    if (subjectNumber, loopSize-1) in D:
        prev = D[(subjectNumber, loopSize-1)]
        prev = subjectNumber * prev
        prev = prev % 20201227
        D[(subjectNumber, loopSize)] = prev
        return prev

    acc = 1
    for i in range(loopSize):
        acc = subjectNumber * acc
        acc = acc % 20201227
        D[(subjectNumber, loopSize)] = acc
    return acc

# CARDS PUBLIC KEY CPK = transferSubjectNumber(7, cardLoopSize) <- cards do that
# DOORS PUBLIC KEY DPK = transferSubjectNumber(7, doorsLoopSize) <-- doors do that
# SHARE (you have both public keys, but neither device's loop size.)
# cardsEncryptionKey = transferSubjectNumber(DPK, cardsLoopSize)
# doorsEncryptionKey = transferSubjectNumber(CPK, doorsLoopSize)


CPK = 19241437
DPK = 17346587
#
# for i in range(10000, 20000):
#     for j in range(1, 1000):
#         cardsEncryptionKey = transferSubjectNumber(CPK, i)
#         doorsEncryptionKey = transferSubjectNumber(DPK, j)
#         if cardsEncryptionKey == doorsEncryptionKey:
#             print(i, j)
#             assert False

#
# for i in range(1, 20_201_227+5):
#     x = transferSubjectNumber(7, i)
#     if i % 1000 == 0:
#         print("iter " + str(i))
#     if CPK == transferSubjectNumber(7, i):
#         print(i)
#         break

xx = 8808305



# for i in range(1, 20_201_227+5):
#     x = transferSubjectNumber(7, i)
#     if i % 1000 == 0:
#         print("iter " + str(i))
#     if 17346587 == x:
#         print(i)
#         break

yy = 11570336


print(transferSubjectNumber(CPK, xx))
print(transferSubjectNumber(CPK, yy))
print("")
print(transferSubjectNumber(DPK, xx))
print(transferSubjectNumber(DPK, yy))


# print(transferSubjectNumber(5764801, 11))
# print(transferSubjectNumber(17807724, 8))

