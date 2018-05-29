with open("in", "r") as infile:
    input = infile.read()
locations = set()
curX = 0
curY = 0
locations.add((0,0))
part1 = 1
for i in input:
    if(i == '^'):
        curY+=1
    elif(i == 'v'):
        curY-=1
    elif(i == '<'):
        curX-=1
    elif(i == '>'):
        curX+=1
    if((curX, curY) not in locations):
        locations.add((curX, curY))
        part1 += 1

santaX = 0
santaY = 0
roboX = 0
roboY = 0
locations = set()
locations.add((0,0))
part2 = 1

for i in range(len(input)):
    tChar = input[i]
    if(i%2==0):
        if(tChar == '^'):
            santaY+=1
        elif(tChar == 'v'):
            santaY-=1
        elif(tChar == '<'):
            santaX-=1
        elif(tChar == '>'):
            santaX+=1
        if((santaX, santaY) not in locations):
            locations.add((santaX, santaY))
            part2 += 1
    else:
        if(tChar == '^'):
            roboY+=1
        elif(tChar == 'v'):
            roboY-=1
        elif(tChar == '<'):
            roboX-=1
        elif(tChar == '>'):
            roboX+=1
        if((roboX, roboY) not in locations):
            locations.add((roboX, roboY))
            part2 += 1
print("Part 1: {}\nPart 2: {}".format(part1,part2))

