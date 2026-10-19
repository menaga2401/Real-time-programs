#12th program- Compund interest Calculator
a=float(input("Enter principal amount:"))
b=float(input("Enter interest rate:"))
c=float(input("Enter time in years:"))
amount=a*(1+b/100)**c
ci=amount-a
print("Compound Interest =",ci)
print("Total amount =",amount)
