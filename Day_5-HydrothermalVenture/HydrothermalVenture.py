import sys

def printGraph(graph):
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if graph[row][col] == 0:
                print(".", end="")
            else:
                print(graph[row][col], end="")
        print()

lines = sys.stdin.readlines()
for i in range(len(lines)-1):
    lines[i] = lines[i][:-1]

# Part 1
print("Part 1:")

sizeX = 0
sizeY = 0
edges = []
for line in lines:
    edges.append([[int(x) for x in vertex.split(",")] for vertex in line.split(" -> ")])

for edge in edges:
    for vertex in edge:
        if vertex[0] > sizeX:
            sizeX = vertex[0]
        if vertex[1] > sizeY:
            sizeY = vertex[1]

graph = [[0 for i in range(sizeX)] for j in range(sizeY)]

print(sizeX)
print(sizeY)

# printGraph(graph)

# Part 2
print("Part 2:")

