#2. Market Survey Analyzer
#Skills: for loop, dicts, counting

pref = ["coffee", "tea", "coffee", "soda", "tea", "coffee"] ###Data collected from survey
for item in set(pref): #for every unie item in the list do the following
    print(f"{item}: {pref.count(item)/len(pref)*100:.0f}%") #prints the item follwoed by how many time it appeared divided by total collected data times 100


