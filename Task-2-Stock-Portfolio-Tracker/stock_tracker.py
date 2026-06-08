stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 380,
    "AMZN": 170
}

portfolio = {}
total_investment = 0

n = int(input("How many stocks do you own? "))

for i in range(n):

    stock = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:

        investment = stock_prices[stock] * quantity

        total_investment += investment

        portfolio[stock] = quantity

    else:
        print("Stock not available.")

print("\nPortfolio Summary")

for stock, quantity in portfolio.items():
    print(stock, "-", quantity, "shares")

print("\nTotal Investment Value: $", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")

    for stock, quantity in portfolio.items():
        file.write(f"{stock}: {quantity} shares\n")

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nData saved to portfolio.txt")