file = open("input.txt", "r")

depth = 0
hor_pos = 0
aim = 0

for line in file:
    line = line.strip()
    line = line.split()
    print(line)

    if line[0] == "forward":
        hor_pos += int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
    elif line[0] == "up":
        depth -= int(line[1])

file.close()
print(depth * hor_pos)