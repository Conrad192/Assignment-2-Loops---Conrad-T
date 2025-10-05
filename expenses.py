# Simulate an employee submitting expenses across categories (Travel, Meals, Supplies).
# Store expenses in a dictionary like:
 

expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}
total =0
for item in expenses: ## print each category with the sum of its expenses
    print(f"{item}: ",sum(expenses[item]))  # prints categories sum totals
    total+=sum(expenses[item]) ## add to the grand total  
print("Grand Total: ", total)

