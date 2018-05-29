import re
with open("in", "r") as infile:
    comm = infile.read().split("\n")

part1 = 0
part2 = 0
realsue = dict()
realsue['children'] = 3
realsue['cats'] = 7
realsue['samoyeds'] = 2
realsue['pomeranians'] = 3
realsue['akitas'] = 0
realsue['vizslas'] = 0
realsue['goldfish'] = 5
realsue['trees'] = 3
realsue['cars'] = 2
realsue['perfumes'] = 1


for i in range(len(comm)):
    testSue = comm[i]
    words = re.split(": |, ", testSue)
    isSue = True
    for j in range(len(words)):
        if(words[j] in realsue):
            if(realsue[words[j]] != int(words[j+1])):
                isSue = False
                break
    if(isSue):
        part1 = i+1
        break


for i in range(len(comm)):
    testSue = comm[i]
    words = re.split(": |, ", testSue)
    isSue = True
    for j in range(len(words)):
        if(words[j] in realsue):
            if(words[j] in ["cats", "trees"]):
                if(realsue[words[j]] >= int(words[j+1])):
                    isSue = False
                    break
            elif(words[j] in ["goldfish", "pomeranians"]):
                if(realsue[words[j]] <= int(words[j+1])):
                    isSue = False
                    break
            elif(realsue[words[j]] != int(words[j+1])):
                isSue = False
                break
    if(isSue):
        part2 = i+1
        break

print("Part 1: {}\nPart 2: {}".format(part1, part2))
