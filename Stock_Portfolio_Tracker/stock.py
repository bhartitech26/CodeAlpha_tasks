# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}
total_investment = 0

# Number of stocks to enter
n = int(input("How many different stocks do you own? "))

# Input stock details
for i in range(n):
    stock_name = input(f"\nEnter stock symbol #{i+1}: ").upper()
    quantity = int(input("Enter quantity: "))

    portfolio[stock_name] = quantity

# Calculate total investment
print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(
            f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}"
        )
    else:
        print(f"{stock}: Price not available")

print("\nTotal Investment Value = $", total_investment)

# Optional: Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-----------------\n")

        for stock, quantity in portfolio.items():
            if stock in stock_prices:
                investment = stock_prices[stock] * quantity
                file.write(
                    f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}\n"
                )

        file.write(f"\nTotal Investment Value = ${total_investment}")

    print("Report saved as 'portfolio_report.txt'")