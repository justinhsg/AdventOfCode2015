from collections import deque
with open("in", "r") as infile:
    comm = infile.read().split("\n")

part1 = 0
part2 = 0

fromPlace = dict()
for i in comm:
    splitComm = i.split(" ")
    place1 = splitComm[0]
    place2 = splitComm[2]
    if(place1 not in fromPlace):
        fromPlace[place1] = len(fromPlace)
    if(place2 not in fromPlace):
        fromPlace[place2] = len(fromPlace)

nNode = len(fromPlace)
dist = [ [0 for i in range(nNode)] for i in range(nNode)]
memory = [ [9999999 for i in range(2**nNode)] for i in range(nNode)]
def listBin(inList):
    op = 0
    for i in range(8):
        if(inList[i]):
            op+=2**i
    return op

def binList(num):
    outList = []
    for i in range(8):
        outList.append(False)
    for i in range(7,-1,-1):
        if( (2**i) <= num):
            outList[i] = True
            num -= 2**i
    return outList

def tsp(end, visited):
    #print("tsp {} {}".format(end,visited))
    if(memory[end][visited] != 9999999):
        return memory[end][visited]
    curList = binList(visited)
    curList[end] = False
    for i in range(len(curList)):
        if(curList[i]):
            memory[end][visited] = min(memory[end][visited], tsp(i, listBin(curList)) + dist[end][i])
    return memory[end][visited]

def atsp(end, visited):
    if(memory[end][visited] != -1):
        return memory[end][visited]
    curList = binList(visited)
    curList[end] = False
    for i in range(len(curList)):
        if(curList[i]):
            memory[end][visited] = max(memory[end][visited], atsp(i, listBin(curList)) + dist[end][i])
    return memory[end][visited]

for i in comm:
    splitComm = i.split(" ")
    place1 = splitComm[0]
    place2 = splitComm[2]
    dist[fromPlace[place1]][fromPlace[place2]] = int(splitComm[4])
    dist[fromPlace[place2]][fromPlace[place1]] = int(splitComm[4])

for i in range(nNode):
    memory[i][2**i] = 0
part1 = 999999999
for i in range(nNode):
    part1 = min(part1, tsp(i,2**nNode-1))
memory = [ [-1 for i in range(2**nNode)] for i in range(nNode)]
for i in range(nNode):
    memory[i][2**i] = 0
part2 = -1
for i in range(nNode):
    part2 = max(part2, atsp(i,2**nNode-1))
print("Part 1: {}\nPart 2: {}".format(part1, part2))
