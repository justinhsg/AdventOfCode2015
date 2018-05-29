from queue import PriorityQueue
with open("in", "r") as infile:
    comm = infile.read().split("\n")


part1 = 0
part2 = 0

bossHP = int(comm[0].split(" ")[-1])
bossDamage = int(comm[1].split(" ")[-1])
playerHP = 50
print(bossDamage)
print(bossHP)
pq = PriorityQueue()
pq.put((0, 500, bossHP, 50, 0, 0, 0, True))
while(not pq.empty()):
    curState = pq.get()
    usedMana = curState[0]
    manaLeft = curState[1]
    bossHealth = curState[2]
    playerHealth = curState[3]
    shieldTime = curState[4]
    poisonTime = curState[5]
    rechargeTime = curState[6]
    isPlayerTurn = curState[7]
    if(shieldTime != 0):
        shieldTime -= 1
    if(poisonTime != 0):
        poisonTime -= 1
        bossHealth -= 3
    if(rechargeTime != 0):
        rechargeTime -= 1
        manaLeft += 101
    if(bossHealth <= 0):
        part1 = usedMana
        break

    if(isPlayerTurn):
        #Magic Missile
        if(manaLeft >= 53):
            #print("Cast Magic Missile")
            tmanaLeft = manaLeft - 53
            tusedMana = usedMana + 53
            tbossHealth = bossHealth - 4
            if(tbossHealth <= 0):
                part1 = tusedMana
                break

            pq.put((tusedMana, tmanaLeft, tbossHealth, playerHealth, shieldTime, poisonTime, rechargeTime, False))
        #Drain
        if(manaLeft >= 73):
            #print("Cast Drain")
            tmanaLeft = manaLeft - 73
            tusedMana = usedMana + 73
            tbossHealth = bossHealth - 2
            tplayerHealth = playerHealth + 2
            if(tbossHealth <= 0):
                part1 = tusedMana
                break
            pq.put((tusedMana, tmanaLeft, tbossHealth, tplayerHealth, shieldTime, poisonTime, rechargeTime, False))
        #Shield
        if(manaLeft >= 113 and shieldTime == 0):
            #print("Cast Shield")
            tmanaLeft = manaLeft - 113
            tusedMana = usedMana + 113
            tshieldTime = 6
            pq.put((tusedMana, tmanaLeft, bossHealth, playerHealth, tshieldTime, poisonTime, rechargeTime, False))
        #Poison
        if(manaLeft >= 173 and poisonTime == 0):
            #print("Cast Poison")
            tmanaLeft = manaLeft - 173
            tusedMana = usedMana + 173
            tpoisonTime = 6
            pq.put((tusedMana, tmanaLeft, bossHealth, playerHealth, shieldTime, tpoisonTime, rechargeTime, False))
        #recharge
        if(manaLeft >= 229 and rechargeTime == 0):
            #print("Cast Recharge")
            tmanaLeft = manaLeft - 229
            tusedMana = usedMana + 229
            trechargeTime = 5
            pq.put((tusedMana, tmanaLeft, bossHealth, playerHealth, shieldTime, poisonTime, trechargeTime, False))
    else:
        if(shieldTime > 0):
            playerHealth -= (bossDamage - 7)
        else:
            playerHealth -= bossDamage
        if(playerHealth > 0):
            pq.put((usedMana, manaLeft, bossHealth, playerHealth, shieldTime, poisonTime, rechargeTime, True))

pq = PriorityQueue()
pq.put((0, 500, bossHP, 50, 0, 0, 0, True))


while(not pq.empty()):
    curState = pq.get()
    usedMana = curState[0]
    manaLeft = curState[1]
    bossHealth = curState[2]
    playerHealth = curState[3]
    shieldTime = curState[4]
    poisonTime = curState[5]
    rechargeTime = curState[6]
    isPlayerTurn = curState[7]
    if(shieldTime != 0):
        shieldTime -= 1
    if(poisonTime != 0):
        poisonTime -= 1
        bossHealth -= 3
    if(rechargeTime != 0):
        rechargeTime -= 1
        manaLeft += 101
    if(bossHealth <= 0):
        part2 = usedMana
        break

    if(isPlayerTurn):
        playerHealth -= 1
        if(playerHealth == 0):
            continue
        #Magic Missile
        if(manaLeft >= 53):
            #print("Cast Magic Missile")
            tmanaLeft = manaLeft - 53
            tusedMana = usedMana + 53
            tbossHealth = bossHealth - 4
            if(tbossHealth <= 0):
                part2 = tusedMana
                break

            pq.put((tusedMana, tmanaLeft, tbossHealth, playerHealth, shieldTime, poisonTime, rechargeTime, False))
        #Drain
        if(manaLeft >= 73):
            #print("Cast Drain")
            tmanaLeft = manaLeft - 73
            tusedMana = usedMana + 73
            tbossHealth = bossHealth - 2
            tplayerHealth = playerHealth + 2
            if(tbossHealth <= 0):
                part2 = tusedMana
                break
            pq.put((tusedMana, tmanaLeft, tbossHealth, tplayerHealth, shieldTime, poisonTime, rechargeTime, False))
        #Shield
        if(manaLeft >= 113 and shieldTime == 0):
            #print("Cast Shield")
            tmanaLeft = manaLeft - 113
            tusedMana = usedMana + 113
            tshieldTime = 6
            pq.put((tusedMana, tmanaLeft, bossHealth, playerHealth, tshieldTime, poisonTime, rechargeTime, False))
        #Poison
        if(manaLeft >= 173 and poisonTime == 0):
            #print("Cast Poison")
            tmanaLeft = manaLeft - 173
            tusedMana = usedMana + 173
            tpoisonTime = 6
            pq.put((tusedMana, tmanaLeft, bossHealth, playerHealth, shieldTime, tpoisonTime, rechargeTime, False))
        #recharge
        if(manaLeft >= 229 and rechargeTime == 0):
            #print("Cast Recharge")
            tmanaLeft = manaLeft - 229
            tusedMana = usedMana + 229
            trechargeTime = 5
            pq.put((tusedMana, tmanaLeft, bossHealth, playerHealth, shieldTime, poisonTime, trechargeTime, False))
    else:
        if(shieldTime > 0):
            playerHealth -= (bossDamage - 7)
        else:
            playerHealth -= bossDamage
        if(playerHealth > 0):
            pq.put((usedMana, manaLeft, bossHealth, playerHealth, shieldTime, poisonTime, rechargeTime, True))


#Format (usedmana, manaleft, bossHP, playerHP, shield-timer, poison-timer, recharge-timer)

print("Part 1: {}\nPart 2: {}".format(part1, part2))