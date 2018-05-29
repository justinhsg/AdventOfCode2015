from collections import deque
with open("in", "r") as infile:
    comm = infile.read()


def charInt (c):
    return ord(c) - ord('a')
password = []
for i in comm:
    password.append(charInt(i))

def intChar(i):
    return chr(i+ord('a'))


def isValid():
    if(8 in password or 11 in password or 14 in password):
        return False
    possiblyValid = False
    for i in range(len(password)-2):
        if(password[i] == password[i+1]-1 and password[i] == password[i+2]-2):
            possiblyValid = True
            break
    if(not possiblyValid):
        return False
    else:
        pair1 = -1
        for i in range(len(password)-1):
            if(password[i] == password[i+1]):
                pair1 = password[i]
                break
        if(pair1 == -1):
            return False
        else:
            for i in range(len(password)-1):
                if(password[i] == password[i+1] and password[i] != pair1):
                    return True
                    break
            return False



def increment(idx):
    global password
    trueIdx = len(password)-1 - idx
    if (trueIdx == -1):
        password = [0] + password
    else:
        password[trueIdx] += 1
        if(password[trueIdx]==26):
            password[trueIdx] = 0
            increment(idx+1)

while(True):
    increment(0)
    if(isValid()):
        break

part1 = ''
for i in password:
    part1 += intChar(i)

while(True):
    increment(0)
    if(isValid()):
        break

part2 = ''
for i in password:
    part2 += intChar(i)


print("Part 1: {}\nPart 2: {}".format(part1, part2))
