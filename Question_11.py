# Write a program to check if a list contains a palindrome of elements.

list = [1,2,2,1]

list2  = list.copy()
list2.reverse()

if(list2 == list):
    print("Palindrome")
else:
    print("Not a palindrome")