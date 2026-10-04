pin = int(input("Enter PIN: "))
balance = 5000

if pin == 1234:

    print("Access granted")

    amount = int(input("Withdraw amount: "))

    if amount <= balance:
        print("Collect your money")

    else:
        print("Not enough balance")

else:
    print("Wrong PIN")