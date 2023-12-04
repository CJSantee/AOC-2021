import sys

lines = sys.stdin.readlines()

n = int(lines[0])
arr = [int(x) for x in lines[1].split()]

# WORKING SOLUTION
# for loop in range(n):
#     for i in range(len(arr)-1):
#         if ((arr[i]+arr[i+1])%2==0):
#             arr.pop(i)
#             arr.pop(i)
#             break
# print(len(arr))

removeIndicies = set()
for i in range(n-1):
    if (i in removeIndicies):
        continue
    if ((arr[i]+arr[i+1])%2==0):
        removeIndicies.add(i)
        removeIndicies.add(i+1)
        # print("REMOVING %i and %i"%(i, i+1))
        beforeIdx = i-1
        afterIdx = i+2
        while (beforeIdx >=0 and afterIdx < len(arr)):
            if (beforeIdx in removeIndicies or afterIdx in removeIndicies):
                break
            if ((arr[beforeIdx]+arr[afterIdx])%2==0):
                removeIndicies.add(beforeIdx)
                removeIndicies.add(afterIdx)
                beforeIdx -= 1
                afterIdx += 1
            else: 
                break
# print(removeIndicies)

print(n-len(removeIndicies))