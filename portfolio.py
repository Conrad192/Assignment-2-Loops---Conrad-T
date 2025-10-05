import random


portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}
total_value = 0
for stock, price, in portfolio.items():  #finds total value of portfolio
    stock_value = price["shares"] * price["price"]
    total_value += stock_value

print("Stock values with ±5% random changes:")
i=1
while i<=7: #runs for 7 days
    print("Day ",i,":")
    for stock, info in portfolio.items():
        # Calculate new random price
        new_price = info["price"] * random.uniform(0.95, 1.05)  #new share val
        stock_value = info["shares"] * new_price #total stock price in portfolio
        
        print(f"{stock}: ${stock_value:.2f}") # prints each stock and value every day
    i+=1
# Bonus: simulate a week of random daily price changes (±5%) and reprint total value each day.


