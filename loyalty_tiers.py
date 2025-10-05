
customers = {"Alice": 800, "Bob": 1500, "Carol": 6000, "David": 300, "Eve": 4500}
Ranks = {"Bronze": 0, "Silver": 0, "Gold": 0}
for customer, spending in customers.items(): 
    if spending <1000:
        Ranks["Bronze"] +=1  # Bronze (< $1000)

    elif 1000 <= spending <5000:
            Ranks["Silver"] +=1   # Silver ($1000–$4999)

    else:
            Ranks["Gold"] +=1    # Gold ($5000+)

 
print(Ranks)



