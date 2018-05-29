with open("in", "r") as infile:
    comm = infile.read().split("\n")

part1 = 0
part2 = 0
MAXVOL = 150
containers = list(map(int, comm))
combis = []
for i in range(1<<len(containers)):
    tVal = 0
    for j in range(len(containers)):
        if(i & 1<<j != 0):
            tVal += containers[j]
            if(tVal > MAXVOL):
                break
    if(tVal == MAXVOL):
        part1 += 1
        combis.append(i)
nContainers = len(containers)+1
for i in combis:
    tContainers = 0
    for j in range(len(containers)):
        if(i & 1<<j != 0):
            tContainers += 1
    if(tContainers < nContainers):
        part2 = 1
        nContainers = tContainers
    elif(tContainers == nContainers):
        part2 += 1







print("Part 1: {}\nPart 2: {}".format(part1, part2))
