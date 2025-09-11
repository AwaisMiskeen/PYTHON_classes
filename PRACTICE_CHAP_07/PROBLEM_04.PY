# Write a program to find whether a given number is prime or not?

num = int(input("Enter Your Number: "))

for i in range(2, num):
    if(num % i) == 0:
        print("Your number is not prime")
        break
    
else:
    print("Your number is prime")
