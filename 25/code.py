with open("in", "r") as infile:
    comm = infile.read().split(" ")

rowN = int(comm[-3][:-1])
colN = int(comm[-1][:-1])

MULVALUE = 252533
DIVVALUE = 33554393
codeN = int((rowN+colN)*(rowN+colN-1)/2 - (rowN-1))

tCode = 1
tVal = 20151125
while(tCode != codeN):
    tCode += 1
    tVal = (tVal*MULVALUE)%DIVVALUE

part1 = tVal
print("Answer: {}".format(part1))
