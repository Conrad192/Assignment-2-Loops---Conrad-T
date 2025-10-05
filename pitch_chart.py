
rev = float(input("Enter initial revenue: $"))
growth_rate = float(input("Enter annual growth rate (%): "))
i=1
while i <=10:
    rev = rev * (1 + growth_rate / 100)
    print("Year ",i,": ","#"*int(rev/100)) #prints hashtag for every 100 dollars of rev every year
    i+=1
