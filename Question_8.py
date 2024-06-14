#Write a program to find the greatest of 3 numbers entered by the user

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secound number: "))
num3 = int(input("Enter the thired number: "))

if(num1 > num2 and num1 > num3):
    print(num1,"is greater than other numbers")
elif(num2 > num1 and num2 > num3):
    print(num2,"is greater than other numbers")
elif(num3 > num1 and num3 >num2):
    print(num3,"is greater than other numbers")
else:
    print("Invalid choice")