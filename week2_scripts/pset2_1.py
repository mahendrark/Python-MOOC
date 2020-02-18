# Week 2 PSET 1 Paying Debt off in a Year 
# Program to calculate the credit card balance after one year if a person only pays...
# ...the minimum monthly payment required by the credit card company each month.

balance = float(input("Initial outstanding balance: "))
annualInterestRate = float(input("Annual interest rate on the sum lent: "))
monthlyPaymentRate = float(input("Minimum monthly payment rate: "))


monthlyInterestRate = (annualInterestRate) / 12.0
unpaidBal = balance

for n in range(12):
    monthlyMinPay = unpaidBal * monthlyPaymentRate
    unpaidBal = unpaidBal - monthlyMinPay
    interestAcrued = unpaidBal * monthlyInterestRate
    unpaidBal = unpaidBal + interestAcrued

print("Remaining balance: "+str(round(unpaidBal, 2)))
