""" Stock Market Profits"""

days = int(input("Enter the number of days: ")) # num of days for the stock prices given
prices = [] # list to store the stock prices

for i in range(1, days+1): # loop to get the stock prices for each day
    value = int(input("Enter the price of the stock on day " + str(i) + ": "))
    if value > 0:
        prices.append(value) # add the stock price to its unique day
    else: # if the stock price is negative or zero, the program will restart
        print("Invalid input. Enter a positive number.")
        break

def max_profit(prices):
    '''Function to calculate the maximum profit that can be made from the stock prices'''
    min_price = prices[0] # first day price
    min_day = 1 # day 1
    maxprofit = 0 # initial profit
    buy_day = 1 # initial buy day
    sell_day = 1 # initial sell day

    for j in range(1, len(prices)): # loop to calculate the maximum profit
        if prices[j] < min_price: # if the price is less than the minimum price
            min_price = prices[j] # update the minimum price
            min_day = j + 1 # update the day
        elif prices[j] - min_price > maxprofit: # for the maximum profit
            maxprofit = prices[j] - min_price # update the maximum profit
            buy_day = min_day # update the buy day
            sell_day = j + 1 # update the sell day

    return maxprofit, buy_day, sell_day

profit, buyday, sellday = max_profit(prices) # to set the return values to the variables
if profit > 0: # if there is a profit
    print(f"Maximum profit: {profit} $")
    print(f"Buy on day {buyday} and sell on day {sellday}")
else: # if there is no profit
    print("No profit can be made")
# we can also add the print lines inside the function
#  but the main goal was for the function to return
