import json
import re
with open("in", "r") as infile:
    comm = infile.read()


numbers = list(map(int,re.findall(r"-?\d+", comm)))
part1 = sum(numbers)

def isnum(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def parse(obj):
    if(type(obj) == type(0)):
        return obj
    elif(type(obj) == type('')):
        if(isnum(obj)):
            return int(obj)
        else:
            return 0
    elif(type(obj) == type([])):
        returnValue = 0
        for i in obj:
            returnValue += parse(i)
        return returnValue
    elif(type(obj) == type({})):
        vals = list(obj.values())
        if("red" in vals):
            return 0
        else:
            returnValue = 0
            for i in vals:
                returnValue += parse(i)
            return returnValue


jsonobj = json.loads(comm)
part2 = parse(jsonobj)

print("Part 1: {}\nPart 2: {}".format(part1, part2))
