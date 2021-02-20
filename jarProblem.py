totalCandies = 10
numberOfCandiesSold = int(input())
if numberOfCandiesSold in range(1,6):
    print(f"Number of Candies sold : {numberOfCandiesSold}")
    print(f'Number of Candies Availabe: {totalCandies - numberOfCandiesSold}')
else:
    print('Invalid Input')
    print(f'Number of Candies Left {totalCandies}')