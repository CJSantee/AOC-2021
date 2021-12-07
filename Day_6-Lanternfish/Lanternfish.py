import sys

lines = sys.stdin.readlines()
for i in range(len(lines)-1):
    lines[i] = lines[i][:-1]

# Part 1
print("Part 1:")
fish = [int(x) for x in lines[0].split(',')]

days = 80
# print(fish)
for day in range(days):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1
    # print(fish)
print(len(fish))
        
# Part 2
print("Part 2:")

fish = [int(x) for x in lines[0].split(',')]

days = [0] * 9
# Update the current numbers
for f in fish:
    days[f] += 1

for i in range(256):
    # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8    
    today = i % len(days)
    # Add new babies
    days[(today + 7) % len(days)] += days[today]

print(sum(days))
