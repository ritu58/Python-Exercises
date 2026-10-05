correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:

    if password == correct_password:
        print("Login successful")
        print("Welcome Admin")

    else:
        print("Wrong password")

else:
    print("User does not exist")