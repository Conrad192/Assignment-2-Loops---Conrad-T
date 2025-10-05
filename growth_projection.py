
rev = float(input("Enter initial revenue: $"))
growth_rate = float(input("Enter annual growth rate (%): "))
i=0
while i <10:
    rev = rev * (1 + growth_rate / 100)
    print(f"Year {i+1}: ${rev:.2f}")
    i+=1

