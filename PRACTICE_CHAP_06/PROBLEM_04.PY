# Write a program to find whether a given username contains less than 10
# characters or not?

username = input("Enter username:")

if(len(username)<10):
    print("Your user name contain less then 10 characters: \n\t",username)

else:
    print("your user name is good:\n\t",username)