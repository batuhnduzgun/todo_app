title = input("Enter your title: ")

length = len(title)

if length <= 100 :
    print("Your title length is", length)
else:
    print("Your title is longer than 100 characters.")