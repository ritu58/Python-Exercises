print("Hello Python")
print("I am learning Python in VS Code")
number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
else:
    print("Negative number")
    a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operator = input("Enter operator (+,-,*,/): ")

if operator == "+":
    print(a + b)

elif operator == "-":
    print(a - b)

elif operator == "*":
    print(a * b)

elif operator == "/":
    print(a / b)

else:
    print("Invalid operator")