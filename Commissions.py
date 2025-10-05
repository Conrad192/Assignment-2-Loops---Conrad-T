sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

def getCommission(sales): #Converts sales to commissions at 10%
    commissions = {}
    for name in sales:
        commissions[name] = sales[name] * 0.1
    return commissions

def sortedCommissions(sales_dict):  #Sorts commissions from highest to lowest
    commissions = getCommission(sales_dict)
    sorted_commissions = dict(sorted(commissions.items(), key=lambda item: item[1], reverse=True))
    return sorted_commissions

# Get the leaderboard of commissions
leaderBoard = sortedCommissions(sales)

# Print the results in leader board formation
print("Commission Leaderboard:")
print("-" * 25)

x=1
for name, commission in leaderBoard.items():
    print(x,f".{name}: ${commission:.2f}") #prints name followed by the comission amount for the lenght of the DICT
    x+=1