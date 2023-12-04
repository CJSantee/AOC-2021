import sys

lines = sys.stdin.readlines()

nums = [int(x) for x in lines[0].split()]

a = nums[0]
b = nums[1]
h = nums[2]

traveled = 0
count = 0
while (traveled < h):
    traveled += a
    count += 1
    if (traveled >= h):
        break
    traveled -= b
    
print(count)