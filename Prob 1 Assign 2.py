
x = .0001
prices = [] ##Store prices in a list.
while x!=0:
    x = float(input("Enter the price of your item and enter 0 when finished: -> ")) ##Ask customers to enter the price of items they’re buying (loop until they enter 0).
    
    prices.append(x)

print (prices) #Prints list
print("total: $", sum(prices)) ##total purchase amount
print("avg item cost: ", sum(prices)/len(prices))##average item cost
print("# of items bought : ", len(prices)-1) ##number of items bought

