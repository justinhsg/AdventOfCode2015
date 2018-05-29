from itertools import combinations
from operator import mul
from functools import reduce
with open("in", "r") as infile:
    comm = list(map(int, infile.read().split("\n")))


for i in range(1, len(comm)+1):
    combis = [s for s in list(combinations(comm, i)) if sum(s) == sum(comm)/3]
    if len(combis) > 0:
        break
part1 = reduce(mul, min(combis, key = lambda x: reduce(mul, x)))
for i in range(1, len(comm)+1):
    combis = [s for s in list(combinations(comm, i)) if sum(s) == sum(comm)/4]
    if len(combis) > 0:
        break
part2 = reduce(mul , min(combis, key = lambda x: reduce(mul, x)))
print("Part 1: {}\nPart 2: {}".format(part1, part2))
