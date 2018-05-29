from collections import deque
with open("in", "r") as infile:
    input = infile.read().split("\n")

part1 = 0
part2 = 0
completed = 0
wires = dict()
index = 0
commQ = deque()





for command in input:
    splitComm = command.split(" ")
    commQ.append(splitComm)
for i in range(65536):
    wires[str(i)] = i

while(len(commQ) != 0):
    splitComm = commQ.popleft()
    if(len(splitComm) == 3):
        tFrom = splitComm[0]
        tTo = splitComm[2]
        if(tFrom not in wires):
            commQ.append(splitComm)
        else:
            wires[tTo] = wires[tFrom]
    elif(len(splitComm) == 4):
        tFrom = splitComm[1]
        tTo = splitComm[3]
        if(tFrom not in wires):
            commQ.append(splitComm)
        else:
            wires[tTo] = 65535 - wires[tFrom]
    elif(len(splitComm) == 5):
        param1 = splitComm[0]
        gate = splitComm[1]
        param2 = splitComm[2]
        tTo = splitComm[4]
        if(param1 not in wires or param2 not in wires):
            commQ.append(splitComm)
        else:
            if(gate == "AND"):
                wires[tTo] = wires[param1]&wires[param2]
            elif(gate == "OR"):
                wires[tTo] = wires[param1]|wires[param2]
            elif(gate == "RSHIFT"):
                wires[tTo] = wires[param1]>>wires[param2]
            elif(gate == "LSHIFT"):
                wires[tTo] = wires[param1]<<wires[param2]
            else:
                print(gate)
part1 = wires['a']


wires = dict()
wires['b'] = part1
for i in range(65536):
    wires[str(i)] = i
for command in input:
    splitComm = command.split(" ")
    commQ.append(splitComm)
while(len(commQ) != 0):
    splitComm = commQ.popleft()
    if(len(splitComm) == 3):
        tFrom = splitComm[0]
        tTo = splitComm[2]
        if(tFrom not in wires):
            commQ.append(splitComm)
        elif(tTo != 'b'):
            wires[tTo] = wires[tFrom]
    elif(len(splitComm) == 4):
        tFrom = splitComm[1]
        tTo = splitComm[3]
        if(tFrom not in wires):
            commQ.append(splitComm)
        else:
            wires[tTo] = 65535 - wires[tFrom]
    elif(len(splitComm) == 5):
        param1 = splitComm[0]
        gate = splitComm[1]
        param2 = splitComm[2]
        tTo = splitComm[4]
        if(param1 not in wires or param2 not in wires):
            commQ.append(splitComm)
        else:
            if(gate == "AND"):
                wires[tTo] = wires[param1]&wires[param2]
            elif(gate == "OR"):
                wires[tTo] = wires[param1]|wires[param2]
            elif(gate == "RSHIFT"):
                wires[tTo] = wires[param1]>>wires[param2]
            elif(gate == "LSHIFT"):
                wires[tTo] = wires[param1]<<wires[param2]
            else:
                print(gate)
part2 = wires['a']
print("Part 1: {}\nPart 2: {}".format(part1,part2))