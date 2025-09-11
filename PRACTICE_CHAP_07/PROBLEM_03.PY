# problem no 1:Write a program to print multiplication table of a given number using for loop?

# Attempt problem 1 using while loop?

num = int(input("Enter Number: "))

i = 1

while(i<11):
    print(f"{num} x {i} = {num*i}")
    i += 1