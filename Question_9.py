#Write a program to check if a number is multiple of 7 or not

num = int(input("Enter the number: "))

if(num % 7 == 0):
    print("Yes ",num, "is a multiple of 7")
else:
    print("NO",num,"is not a multiple by 7")