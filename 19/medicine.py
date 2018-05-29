with open("in", "r") as infile:
    comm = infile.read().split("\n")

replacements = []
for i in comm[:-2]:
    words = i.split(" => ")
    replacements.append(words)

s = comm[-1]
possibles = set()

for replacement in replacements:
    for i in range(len(s)):
        if s[i:i+len(replacement[0])] == replacement[0] :
            news = s[:i] + replacement[1] + s[i+len(replacement[0]):]
            possibles.add(news)

part1 = len(possibles)
nElements = 0
for i in s:
    if (i.isupper()):
        nElements += 1
nRn = s.count("Rn")
nAr = s.count("Ar")
nY = s.count("Y")
part2 = nElements - nRn - nAr - 2*nY - 1
print("Part 1: {}\nPart 2: {}".format(part1, part2))