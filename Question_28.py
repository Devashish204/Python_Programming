#Write a function to check whether number is even or odd

num = int(input("Enter the number to check whether it is even or odd: "))

def even_odd(val):
    if(val%2 == 0):
        print("Number is even")
    elif(val%2!=0):
        print("Number is odd")
    else:
        print("Invalid")

even_odd(num)