with open("in", "r") as infile:
    comm = infile.read().split("\n")

ENDTIME = 2503
part1 = 0
part2 = 0
names = dict()
reindeer = []
for i in range(len(comm)):
    words = comm[i].split(" ")
    names[words[0]] = i
    speed = int(words[3])
    flytime = int(words[6])
    resttime = int(words[13])
    reindeer.append([speed, flytime,resttime])
for i in range(len(reindeer)):
    nCycles = ENDTIME // (reindeer[i][1] + reindeer[i][2])
    leftover = ENDTIME % (reindeer[i][1] + reindeer[i][2])
    distance = reindeer[i][0]*nCycles*reindeer[i][1] + min(leftover, reindeer[i][1])*reindeer[i][0]
    part1 = max(distance, part1)


points = [0 for i in range(len(reindeer))]
for t in range(1,ENDTIME+1):
    leading = []
    leadDist = 0
    for i in range(len(reindeer)):
        nCycles = t // (reindeer[i][1] + reindeer[i][2])
        leftover = t % (reindeer[i][1] + reindeer[i][2])
        distance = reindeer[i][0]*nCycles*reindeer[i][1] + min(leftover, reindeer[i][1])*reindeer[i][0]
        if(distance > leadDist):
            leadDist = distance
            leading.clear()
            leading.append(i)
        elif(distance == leadDist):
            leading.append(i)
    for i in leading:
        points[i] += 1
part2 = max(points)






print("Part 1: {}\nPart 2: {}".format(part1, part2))
