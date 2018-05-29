with open("in", "r") as infile:
    input = infile.read()


part2 = 0
floor = 0
for i in range(len(input)):
    char = input[i]
    if(char == ")"):
        floor -= 1
    else:
        floor += 1
    if(part2 == 0 and floor == -1):
        part2 = i+1
part1 = floor
print("Part 1: {}\nPart 2: {}".format(part1,part2))