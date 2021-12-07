import sys

lines = sys.stdin.readlines()
for i in range(len(lines)-1):
    lines[i] = lines[i][:-1]


def getBitCount(list):
    bitCount = [0]*(len(list[0]))

    for i in range(len(list)):
        for j in range(len(bitCount)):
            bitCount[j] += int(list[i][j])

    return bitCount

# Part 1
print("Part 1:")

# Power consumption = gamma rate * epsilon rate
bitCount = getBitCount(lines)

gammaRate = ""
epsilonRate = ""
for i in range(len(bitCount)):
    if bitCount[i] > len(lines)/2:
        gammaRate += "1"
        epsilonRate += "0"
    else:
        gammaRate += "0"
        epsilonRate += "1"

print(int(gammaRate, 2) * int(epsilonRate, 2))

# Part 2
print("Part 2:")

checkNow = lines
checkNext = []
ogr = ""
for i in range(len(lines[0])):
    bitCount = getBitCount(checkNow)
    if bitCount[i] >= len(checkNow)/2:
        keep = "1"
    else:
        keep = "0"
    if len(checkNow) != 1:
        for j in range(len(checkNow)):
            if checkNow[j][i] == keep:
                checkNext.append(checkNow[j])
        checkNow = checkNext
        checkNext = []
    else:
        ogr = checkNow[0]
ogr = checkNow[0]
# print(ogr)

checkNow = lines
checkNext = []
csr = ""
for i in range(len(lines[0])):
    bitCount = getBitCount(checkNow)
    if bitCount[i] >= len(checkNow)/2:
        keep = "0"
    else:
        keep = "1"
    if len(checkNow) != 1:
        for j in range(len(checkNow)):
            if checkNow[j][i] == keep:
                checkNext.append(checkNow[j])
        checkNow = checkNext
        checkNext = []
    else:
        csr = checkNow[0]
csr = checkNow[0]
# print(csr)

print(int(ogr, 2) * int(csr, 2))