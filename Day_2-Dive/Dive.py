import sys

lines = sys.stdin.readlines()

# Part 1
print("Part 1:")

horizontal = 0
depth = 0
for line in lines:
    val = line.split()
    if val[0] == "forward":
        horizontal += int(val[1])
    elif val[0] == "down":
        depth += int(val[1])
    else:
        depth -= int(val[1])

print(depth * horizontal)

# Part 2
print("Part 2:")

horizontal = 0
depth = 0
aim = 0
for line in lines:
    val = line.split()
    if val[0] == "forward":
        horizontal += int(val[1])
        depth += aim * int(val[1])
    elif val[0] == "down":
        aim += int(val[1])
    else:
        aim -= int(val[1])

print(depth * horizontal)
