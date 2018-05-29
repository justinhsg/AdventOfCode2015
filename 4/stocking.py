from hashlib import md5
with open("in", "r") as infile:
    input = infile.read()
index = 1
part1 = 0
part2 = 0

while(part1 == 0 or part2 ==0):
    m=md5()
    m.update((input + str(index)).encode())
    hash = m.hexdigest()
    if(hash[:5] == '00000' and part1 == 0):
        part1 = index
    if(hash[:6] == '000000' and part2 == 0):
        part2 = index
    index += 1
print("Part 1: {}\nPart 2: {}".format(part1,part2))