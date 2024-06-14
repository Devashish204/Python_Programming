#Write a program to check if a number entered by the user is odd or even

num = int(input("Enter the number to check whether number is even or odd: "))

if(num > 0):
    if(num%2 == 0):
        print("Number is even.")
    else:
        print("NUmber is odd")
else:
    print("Invalid output")