import sys
arr = [[int(i) for i in x.split()] for x in sys.stdin.readlines()]
count = 0
n = 1
m = 1
count = 0
while (n !=0 and m != 0):
    n = arr[count][0]
    m = arr[count][1]
    count+=1

    print("%i OFFERS"%(n))
    
    bestTix = 0
    bestCost = 0
    bestOffer = sys.maxsize
    for i in range(n):
        tix = arr[count][0]
        cost = arr[count][1]
        count+=1
        offerRate = cost / tix
        
        if (tix > m):
            continue
        print("%i tix for $%i = %.2f" %(tix, cost, offerRate))
        if (offerRate < bestOffer):
            bestOffer = offerRate
            bestTix = tix
            bestCost = cost
        # print(arr[count])
        
    print("Buy %i tickets for $%i" %(bestTix, bestCost))


# print(arr)