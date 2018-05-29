with open("in", "r") as infile:
    comm = infile.read().split("\n")

part1 = 0
part2 = 0
SIZE = 100

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

lights = [list(i) for i in comm]

for n in range(100):
    newlights = [['' for i in range(SIZE)] for i in range(SIZE)]
    for x in range(SIZE):
        for y in range(SIZE):
            nLit = 0
            for d in range(8):
                tx = x+dx[d]
                ty = y+dy[d]
                if(tx >= 0 and ty >= 0 and tx < SIZE and ty < SIZE):
                    if (lights[tx][ty] == '#'):
                        nLit += 1
            if(lights[x][y] == '#'):
                if(nLit == 2 or nLit == 3):
                    newlights[x][y] = '#'
                else:
                    newlights[x][y] = '.'
            else:
                if(nLit == 3):
                    newlights[x][y] = '#'
                else:
                    newlights[x][y] = '.'
    lights = newlights

for x in lights:
    for y in x:
        if (y == '#'):
            part1 += 1

lights = [list(i) for i in comm]
lights[0][0] = '#'
lights[SIZE-1][0] = '#'
lights[0][SIZE-1] = '#'
lights[SIZE-1][SIZE-1] = '#'



for n in range(100):
    newlights = [['' for i in range(SIZE)] for i in range(SIZE)]
    for x in range(SIZE):
        for y in range(SIZE):
            nLit = 0
            for d in range(8):
                tx = x+dx[d]
                ty = y+dy[d]
                if(tx >= 0 and ty >= 0 and tx < SIZE and ty < SIZE):
                    if (lights[tx][ty] == '#'):
                        nLit += 1
            if(lights[x][y] == '#'):
                if(nLit == 2 or nLit == 3):
                    newlights[x][y] = '#'
                else:
                    newlights[x][y] = '.'
            else:
                if(nLit == 3):
                    newlights[x][y] = '#'
                else:
                    newlights[x][y] = '.'
    newlights[0][0] = '#'
    newlights[SIZE-1][0] = '#'
    newlights[0][SIZE-1] = '#'
    newlights[SIZE-1][SIZE-1] = '#'
    lights = newlights

for x in lights:
    for y in x:
        if (y == '#'):
            part2 += 1



print("Part 1: {}\nPart 2: {}".format(part1, part2))
