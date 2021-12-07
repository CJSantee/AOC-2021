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

graph = [[0 for i in range(sizeX+1)] for j in range(sizeY+1)]

printGraph(graph)

for edge in edges:
    if edge[0][1] == edge[1][1]:
        # Horizontal Line
        if edge[0][0] < edge[1][0]:
            src = edge[0][0]
            dest = edge[1][0]
        else:
            src = edge[1][0]
            dest = edge[0][0]
        for col in range(src, dest+1):
            graph[edge[0][1]][col] += 1
    elif edge[0][0] == edge[1][0]:
        # Verticle Line
        if edge[0][1] < edge[1][1]:
            src = edge[0][1]
            dest = edge[1][1]
        else:
            src = edge[1][1]
            dest = edge[0][1]
        for row in range(src, dest+1):
            graph[row][edge[0][0]] += 1
    else:
        # Diagonal Line
        # print("Diagonal Line")
        # print(edge)
        if edge[0][0] < edge[1][0]:
            srcX = edge[0][0]
            destX = edge[1][0]
            srcY = edge[0][1]
            destY = edge[1][1]
            if edge[0][1] < edge[1][1]:
                increasing = True
            else:
                increasing = False
        else:
            srcX = edge[1][0]
            destX = edge[0][0]
            srcY = edge[1][1]
            destY = edge[0][1]
            if edge[1][1] < edge[0][1]:
                increasing = True
            else:
                increasing = False
        # print("(%d, %d) -> (%d, %d)" % (srcX, srcY, destX, destY))
        # if increasing:
        #     print("Increasing")
        # else:
        #     print("Decreasing")
        for i in range(0, (destX-srcX)+1):
            if increasing:
                graph[srcY+i][srcX+i] += 1
            else:
                graph[srcY-i][srcX+i] += 1
        
printGraph(graph)

count = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] >= 2:
            count += 1

print(count) 

# Part 2
# print("Part 2:")

