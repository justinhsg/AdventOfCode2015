from queue import PriorityQueue
with open("in", "r") as infile:
    comm = infile.read().split("\n")


part1 = 0
part2 = 0

seq = []
for i in comm:
    seq.append(i.split(" "))
a = 0
pt = 0
while(pt >= 0 and pt < len(seq)):
    if(pt == 39):
        break
    query = seq[pt][0]
    if(query == "jio"):
        if(a==1):
            pt+=int(seq[pt][2])
        else:
            pt+=1
    elif(query == "inc"):
        a += 1
        pt+= 1
    elif(query == "tpl"):
        a *= 3
        pt+=1
    elif(query == "jmp"):
        pt += int(seq[pt][1])

part1 = 0
while(a!=1):
    part1+=1
    if(a%2 == 0):
        a = a/2
    else:
        a = a*3+1


a = 1
pt = 0
while(pt >= 0 and pt < len(seq)):
    if(pt == 39):
        break
    query = seq[pt][0]
    if(query == "jio"):
        if(a==1):
            pt+=int(seq[pt][2])
        else:
            pt+=1
    elif(query == "inc"):
        a += 1
        pt+= 1
    elif(query == "tpl"):
        a *= 3
        pt+=1
    elif(query == "jmp"):
        pt += int(seq[pt][1])
part2 = 0
while(a!=1):
    part2+=1
    if(a%2 == 0):
        a = a/2
    else:
        a = a*3+1

#Format (usedmana, manaleft, bossHP, playerHP, shield-timer, poison-timer, recharge-timer)

print("Part 1: {}\nPart 2: {}".format(part1, part2))