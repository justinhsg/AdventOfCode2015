from collections import deque
with open("in", "r") as infile:
    input = infile.read().split("\n")

part1 = 0
part2 = 0




for command in input:
    part1 += len(command) - len(eval(command))
    part2 += command.count("\"") + command.count("\\") + 2
print("Part 1: {}\nPart 2: {}".format(part1,part2))