with open("in", "r") as infile:
    input = infile.read().split("\n")
part1 = 0
part2 = 0
for i in range(len(input)):
    dimens = list(map(int,input[i].split("x")))
    part1 += 2*dimens[0]*dimens[1] + 2*dimens[1]*dimens[2] + 2*dimens[0]*dimens[2] + min([dimens[0]*dimens[1], dimens[1]*dimens[2], dimens[0]*dimens[2]])
    part2 += dimens[0]*dimens[1]*dimens[2] + min([dimens[0]+dimens[1], dimens[1]+dimens[2], dimens[0]+dimens[2]])*2
print("Part 1: {}\nPart 2: {}".format(part1,part2))