p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate: "))
t = float(input("Enter time period in years: "))

def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    interest = amount - p
    print("Compound interest is", interest)

compound_interest(p, r, t)