
days = int(input("Enter the number of days: "))
prices = []

for i in range(1, days+1):
    price = int(input("Enter the price of the stock on day " + str(i) + ": "))
    if price > 0:
        prices.append(price)
    else:
        print("Invalid input. Enter a positive number.")
        break

|
