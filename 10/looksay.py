from collections import deque
with open("in", "r") as infile:
    comm = infile.read()

part1 = 0
part2 = 0
s = comm[:]
print(s)
for i in range(50):
    newString = ""
    j = 0
    while(j < len(s)):
        if(j == len(s)-1):
            newString += "1"+s[j]
            break
        elif(j == len(s)-2):
            if(s[j]==s[j+1]):
                newString += "2"+s[j]
            else:
                newString += "1"+s[j]+"1"+s[j+1]
            break
        else:
            if(s[j] == s[j+1] and s[j] == s[j+2]):
                newString += "3"+s[j]
                j+=3
            elif(s[j] == s[j+1]):
                newString += "2"+s[j]
                j+=2
            else:
                newString += "1"+s[j]
                j+=1
    s = newString
    if(i == 39):
         part1 = len(s)
part2 = len(s)
print("Part 1: {}\nPart 2: {}".format(part1, part2))
