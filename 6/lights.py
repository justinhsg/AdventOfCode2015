with open("in", "r") as infile:
    input = infile.read().split("\n")

part1 = 0
part2 = 0
grid = [ [0 for i in range(1000)] for i in range(1000) ]
grid2 = [ [0 for i in range(1000)] for i in range(1000) ]
for i in input:
    comms = i.split(" ")
    start = list(map(int, comms[-3].split(',')))
    end = list(map(int, comms[-1].split(',')))
    if(comms[0] == "toggle"):
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid[x][y] = 0 if grid[x][y] == 1 else 1
                grid2[x][y] += 2
    elif(comms[1] == "on"):
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid[x][y] = 1
                grid2[x][y] += 1
    else:
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid[x][y] = 0
                grid2[x][y] = 0 if grid2[x][y] == 0 else grid2[x][y]-1
for i in range(1000):
    part1+= sum(grid[i])
    part2+= sum(grid2[i])

print("Part 1: {}\nPart 2: {}".format(part1,part2))