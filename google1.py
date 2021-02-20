def gethouses(houses,budget):
    counter = 0
    for x in range(len(houses)):
        if(houses[x] <= budget and budget > 0 ):
            budget = budget - houses[x]
            counter = counter + 1
    houseshebought.append(counter)

auctionRounds = int(input())
housesNL = []
houseshebought = []
totalHB = []
for _ in range(auctionRounds):
    totalHB.append(list(map(int, input().strip().split())))
    housesNL.append(list(map(int, input().strip().split())))
    gethouses(housesNL[_],totalHB[_][1])

for y in range(len(houseshebought)):
    print(f'Case #{y+1}:',houseshebought[y])