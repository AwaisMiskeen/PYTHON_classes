# Write a program to print multiplication table of n using for loops in reversed
# orde?

n = int(input("enter the number: "))

# for i in range(10, 0 ,-1 ):
#     print(f"{n} x {i} = {n * i}")

for i in range (1, 11):
    print(f"{n} x {11-i} = {n*(11-i)}")