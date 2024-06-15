# Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.

marks = {}

maths = int(input("Enter the marks of Maths: "))
marks.update({"Maths": marks})

DAA = int(input("Enter the marks of DAA: "))
marks.update({"DAA": marks})

ADS = int(input("Enter the marks of ADS: "))
marks.update({"ADS": marks})

print(marks)