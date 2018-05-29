from math import ceil
with open("in", "r") as infile:
    comm = infile.read().split("\n")


part1 = 0
part2 = 0

Weapons = [[8 ,4], [10, 5], [25,6], [40,7], [74,8]]
Armor = [[0,0],[13,1],[31,2],[53,3],[75,4],[102,5]]
Rings = [[0,0,0], [0,0,0], [25,1,0], [50,2,0], [100,3,0], [20,0,1],[40,0,2],[80,0,3]]

bossHP = int(comm[0].split(" ")[-1])
bossDamage = int(comm[1].split(" ")[-1])
bossArmor = int(comm[2].split(" ")[-1])
playerHP = 100
part1 = 999999999999999
part2 = -1
for i in range(len(Weapons)):
    for j in range(len(Armor)):
        for k in range(len(Rings)):
            for l in range(len(Rings)):
                if(k == l):
                    continue
                cost = Weapons[i][0] + Armor[j][0] + Rings[k][0] + Rings[l][0]
                playerDamage = Weapons[i][1] + Rings[k][1] + Rings[l][1]
                playerArmor = Armor[j][1] + Rings[k][2] + Rings[l][2]
                if(bossDamage <= playerArmor):
                    bossTurns = 99999999999999
                else:
                    bossTurns = ceil(playerHP / (bossDamage-playerArmor))
                playerTurns = ceil(bossHP / (playerDamage-bossArmor))

                if(playerTurns <= bossTurns):
                    part1 = min(cost, part1)
                else:
                    part2 = max(cost,part2)


print("Part 1: {}\nPart 2: {}".format(part1, part2))