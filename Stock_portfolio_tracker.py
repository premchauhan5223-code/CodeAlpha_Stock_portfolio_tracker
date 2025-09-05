import csv

# Stock prices dictionary
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOG": 120,
    "AMZN": 140,
    "IBM": 135,     
    "ORCL": 90,     
    "INTC": 35, 
    "AMD": 110,     
    "SONY": 85   
}

portfolio = {}

# Take user input
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in prices:
        print(" Stock not available. Try again!")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_value = 0
print("\n Your Portfolio:")

for stock, qty in portfolio.items():
    value = prices[stock] * qty
    total_value += value
    print(f"{stock} - {qty} shares × ${prices[stock]} = ${value}")

print("\n Total Investment Value =", total_value)

# Save results to CSV file
save = input("Do you want to save results to a CSV file? (y/n): ").lower()
if save == "y":
    with open("portfolio.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])  # header row
        for stock, qty in portfolio.items():
            writer.writerow([stock, qty, prices[stock], prices[stock] * qty])
        writer.writerow(["Total", "", "", total_value])
    print(" Results saved to portfolio.csv")
