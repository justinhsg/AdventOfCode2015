with open("in", "r") as infile:
    comm = int(infile.read())

part1 = 0
part2 = 0


houses = [0 for i in range(int(comm//20))]
for i in range(1, int(comm//20)):
    for j in range(i, int(comm//20), i):
        houses[j]+= i*10
    if(houses[i] >= comm):
        part1 = i
        break

houses = [0 for i in range(int(comm//22))]
for i in range(1, int(comm//22)):
    for j in range(i, min(i*51,int(comm//22)) , i):
        if(j < int(comm//22)):
            houses[j] += i*11
    if(houses[i] >= comm):
        part2 = i
        break

print("Part 1: {}\nPart 2: {}".format(part1, part2))