import sys

lines = sys.stdin.readlines()

# Part 1
print("Part 1:")

x = sys.maxsize
count = 0
for line in lines:
    if int(line) > x:
        count += 1
    x = int(line)

print(count)

# Part 2
print("Part 2:")
sums = []
for i in range(len(lines)-2):
    one   = int(lines[i])
    two   = int(lines[i+1])
    three = int(lines[i+2])
    sums.append(one+two+three)

x = sys.maxsize
count = 0
for num in sums:
    if num > x:
        count += 1
    x = num
print(count)

