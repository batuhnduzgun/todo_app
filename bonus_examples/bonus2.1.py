password = input("Enter your password:")

while password != "pass123":
    password = input("This password was wrong! Enter your password:")

print("This password was correct!")