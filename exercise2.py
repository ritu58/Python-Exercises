letter = input("Enter a letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")
else:
    print("Consonant")
    name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
    message = "Excellent"

elif marks >= 80:
    grade = "A"
    message = "Very Good"

elif marks >= 70:
    grade = "B"
    message = "Good"

elif marks >= 50:
    grade = "C"
    message = "Average"

else:
    grade = "F"
    message = "Failed"

print("Student:", name)
print("Grade:", grade)
print(message)
balance = 10000

print("Welcome to ATM")
print("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)

    else:
        print("Insufficient balance")

elif choice == 3:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount

    print("Deposit successful")
    print("New balance:", balance)

else:
    print("Invalid choice")