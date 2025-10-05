

# Model a list of warehouses, each with an inventory dictionary:


warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]
# Write a program that loops through all warehouses to calculate total stock of each product across the supply chain.
total_stock = {}
for warehouse in warehouses:  
    for product, quantity, in warehouse["inventory"].items():
       total_stock[product] = total_stock.get(product, 0) + quantity # looks at each product in each warehouse and increases the toal stock fro that product

print("Total Stock:")
for product, total in total_stock.items():
    print(f"{product}: {total}") 