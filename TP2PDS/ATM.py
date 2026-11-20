balance = 2490
bill_in_machine = {100: 50, 50: 20, 20: 300, 10: 0, 5: 200, 1: 10}

print("=== Welcome to the ATM ===")
while True:

    try:
        amount = int(input("Please input your withdrawal amount: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if amount <= 0 or amount > balance:
        print("Invalid amount. Please enter a valid amount.")
        continue
    left = amount
    #remaining money that the ATM still needs to dispense.

    bill_given = {}
    #This creates an empty dictionary.
    #store the banknotes that the ATM gives to the user.

    for bill in sorted(bill_in_machine, reverse=True):
        count = min(left // bill, bill_in_machine[bill])
        if count > 0:
            bill_given[bill] = count
            left -= bill * count

    if left != 0:
        print("Cannot dispense the requested amount.Try another amount.")
        continue
    break  #valid transaction, exit the loop

for bill, count in bill_given.items():
    bill_in_machine[bill] -= count
balance -= amount

# Print receipt
print("Transaction Successful!")
print(f"You have received ${amount}")
for bill, count in bill_given.items():
    print(f"{count} of ${bill} bill")
print(f"Your remaining balance: ${balance}")
print("Remaining in this machine:")
for bill in sorted(bill_in_machine, reverse=True):
    print(f"${bill} bill cash: {bill_in_machine[bill]} ")
