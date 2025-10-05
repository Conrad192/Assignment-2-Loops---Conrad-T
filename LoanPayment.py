# Skills: while loops, math, functions

# Ask for a loan amount, interest rate, and monthly payment.
# Use a while loop to simulate month-by-month repayment, updating the balance each time.
# Print how many months it takes to pay off the loan.
# 👉 GitHub file: loan_simulator.py

loanAmt= float(input(("Enter Loan Amount: " )) )
intrate = float(input(("Enter Interest Rate (APY%): " )))
monthpmt =float(input(("Enter Monthly Payment: " )))

principal = (loanAmt)
month = 1
while principal>0:
    if monthpmt>principal: #makes sure doesnt over pay
        monthpmt=principal
    principal = principal-monthpmt
    principal = principal + (principal*(intrate/100)/12)
    print(f"(month {month}: Remaining balance: ${principal:.2f})") # repeats every moth taking away monthly payment then adding principal
    month +=1

print(f"It will take {month} months to pay off the loan.")
