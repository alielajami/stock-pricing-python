
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
    min_price = prices[0]
    min_day = 1
    max_profit = 0
    buy_day = 1
    sell_day = 1

    for j in range(1, len(prices)):
        if prices[j] < min_price:
            min_price = prices[j]
            min_day = j + 1
        elif prices[j] - min_price > max_profit:
            max_profit = prices[j] - min_price
            buy_day = min_day
            sell_day = j + 1

    return max_profit, buy_day, sell_day

profit, buy_day, sell_day = max_profit(prices)
if profit > 0:
    print(f"Maximum profit: {profit} $")
    print(f"Buy on day {buy_day} and sell on day {sell_day}")
else:
    print("No profit can be made")
# we can also add the print lines inside the function but the main goal was for the function to return
