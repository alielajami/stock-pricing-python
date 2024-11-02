""" Stock Market Profits"""

days = int(input("Enter the number of days: "))
prices = []

for i in range(1, days+1):
    value = int(input("Enter the price of the stock on day " + str(i) + ": "))
    if value > 0:
        prices.append(value)
    else:
        print("Invalid input. Enter a positive number.")
        break

def max_profit(prices):
    '''Function to calculate the maximum profit that can be made from the stock prices'''
    min_price = prices[0]
    min_day = 1
    maxprofit = 0
    buy_day = 1
    sell_day = 1

    for j in range(1, len(prices)):
        if prices[j] < min_price:
            min_price = prices[j]
            min_day = j + 1
        elif prices[j] - min_price > maxprofit:
            maxprofit = prices[j] - min_price
            buy_day = min_day
            sell_day = j + 1

    return maxprofit, buy_day, sell_day

profit, buyday, sellday = max_profit(prices)
if profit > 0:
    print(f"Maximum profit: {profit} $")
    print(f"Buy on day {buyday} and sell on day {sellday}")
else:
    print("No profit can be made")
# we can also add the print lines inside the function
#  but the main goal was for the function to return
