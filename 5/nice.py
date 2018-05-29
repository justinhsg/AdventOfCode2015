
with open("in", "r") as infile:
    input = infile.read().split("\n")

part1 = 0
part2 = 0

for word in input:
    if ('ab' in word or 'cd' in word or 'pq' in word or 'xy' in word):
        continue
    else:
        if(word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u') >= 3):
            for i in range(len(word)-1):
                if(word[i] == word[i+1]):
                    part1+=1
                    break
for word in input:
    possiblyNice = False
    for i in range(len(word)-1):
        if(word.count(word[i]+word[i+1]) > 1):
            possiblyNice = True
    if(possiblyNice):
        for i in range(len(word)-2):
            if(word[i] == word[i+2]):
                part2+=1
                break
print("Part 1: {}\nPart 2: {}".format(part1,part2))