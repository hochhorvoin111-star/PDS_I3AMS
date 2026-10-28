#  Problem 9. Electricity Bill with Progressive Tiers 

"""
An electricity company charges each kWh according to the tier it falls in, like income tax. 
A fixed service fee of 2,000 riel is added, then 10 % VAT is applied to the total.
(a) Write electricity_bill(kwh) that returns the bill in riel, rounded to a whole number, or None for negative input. 
(b) Print a table for 0, 35, 50, 120, 200 and 350 kWh, with thousands separators (f"{bill:,}") and the value in USD (1 USD = 4,100 riel). 
(c) Ask the user for their monthly consumption and print their bill. 

"""

# (a) electricity bill
def electricity_bill(kwh):
    if kwh < 0:
        return None

    tier1 = min(kwh, 50)                 # first 50 kWh
    tier2 = min(max(kwh - 50, 0), 150)   # next 150 kWh
    tier3 = max(kwh - 200, 0)            # everything above 200 kWh

    total = tier1 * 480 + tier2 * 610 + tier3 * 730
    total = total + 2000                 # fixed service fee
    total = total * 1.10                 # 10% VAT
    return round(total)


# (b) table
for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill / 4100
    print(f"{kwh:>3} kWh -> {bill:>8,} riel  (≈ {usd:>6.2f} USD)")


# (c) ask the user
text = input("Enter your monthly consumption in kWh: ")
try:
    kwh = float(text)
    bill = electricity_bill(kwh)
    if bill is None:
        print("Consumption cannot be negative.")
    else:
        print(f"Your bill is {bill:,} riel (≈ {bill / 4100:.2f} USD)")
except ValueError:
    print("Please type a number.")