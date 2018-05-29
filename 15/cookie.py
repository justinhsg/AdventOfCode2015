with open("in", "r") as infile:
    comm = infile.read().split("\n")

ingredients = []

for i in comm:
    words = i.split(" ")
    ingredients.append([ int(words[2][:-1]), int(words[4][:-1]), int(words[6][:-1]), int(words[8][:-1]), int(words[10]) ])
part1 = 0
part2 = 0
for i in range(100):
    for j in range(100-i):
        for k in range(100-i-j):
            sums = []
            for l in range(5):
                sums.append(max(0, ingredients[0][l]*i + ingredients[1][l]*j + ingredients[2][l]*k + ingredients[3][l]*(100-i-j-k)))
            if(0 not in sums):
                part1 = max(part1, sums[0]*sums[1]*sums[2]*sums[3])
                if(sums[4] <= 500):
                    part2 = max(part2, sums[0]*sums[1]*sums[2]*sums[3])





print("Part 1: {}\nPart 2: {}".format(part1, part2))