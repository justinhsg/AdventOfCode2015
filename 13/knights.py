with open("in", "r") as infile:
    comm = infile.read().split("\n")
part1 = 0
part2 = 0

nPeople = int((len(comm) + 0.25) ** 0.5 + 0.5)



happiness = [[0 for i in range(nPeople)] for i in range(nPeople)]
weights = [[0 for i in range(nPeople)] for i in range(nPeople)]
memory = [[-1000000 for i in range(1 << nPeople)] for i in range(nPeople)]
def tsp(endPerson, visited):
    if(memory[endPerson][visited] != -1000000):
        return memory[endPerson][visited]
    visited = visited & ~(1<<endPerson)
    for i in range(nPeople):
        if(visited & 1 << i != 0):
            memory[endPerson][visited] = max(memory[endPerson][visited], tsp(i, visited) + weights[i][endPerson])
    return memory[endPerson][visited]



for i in comm:
    words = i.split(" ")
    value = int(words[3]) * (1 if words[2] == "gain" else -1)
    receiver = ord(words[0][0]) - ord('A') if words[0][0] != "M" else 7
    giver = ord(words[-1][0]) - ord('A') if words[-1][0] != "M" else 7
    happiness[receiver][giver] = value
for i in range(nPeople):
    for j in range(nPeople):
        weights[i][j] = happiness[i][j] + happiness[j][i]

for i in range(nPeople):
    memory[i][1 << i] = weights[0][i]

for i in range(0, nPeople):
    memory = [[-1000000 for i in range(1 << nPeople)] for i in range(nPeople)]
    for j in range(0, nPeople):
        memory[j][1<<j] = weights[j][i]
    for j in range(0, nPeople):
        if(i!=j):
            tvalue = tsp(j, (1<<nPeople)-1-(1<<i))
            part2 = max(part2, tvalue)
            if(i==0):
                part1 = max(part1, tvalue+weights[j][i])





print("Part 1: {}\nPart 2: {}".format(part1, part2))
