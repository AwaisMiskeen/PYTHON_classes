# if elif else ladder statement

a = int(input("Enter your age: "))

if(a>18):
    print("You are above the age of consent")
    print("Good for you")

elif(a>=18):
    print("You are equal the age of consent")
    print("Good for you")

elif(a==0):
    print("Invailed age you enter 0")

elif(a<0):
    print("Invailed you enter negative age")
else :
    print("You are below the age of consent")

print("end of program")