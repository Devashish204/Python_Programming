#write a program to find the factorial of first n numbers.(using for)

n = int(input("Enter the number to find factorial: "))
factorial =1
for i in range(1,n+1):
    factorial = factorial * i
print(factorial)