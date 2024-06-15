str = "Devashish"

#1. str.endswith("")

print(str.endswith("sh"))
#or
print(str.endswith("hs"))

#endswith always give output in boolean

#2. str.capitalize: it means it converts the first letter of the sting into the uppercase.

str = "rajput"

print(str.capitalize())
print(str)

#capitalize does not change the original string it creates the new string.
#if we want to change the original string than

str = str.capitalize()
print(str)

#3. str.replace(old,new)

str3 = "Devashish Rajput"
print(str3.replace('Devashish','Dev')) 
print(str3)

#here again original string does not affected if you want to replace it with the old one than

str3 = str3.replace('Devashish','Dev')
print(str3)

#we can also replace only specific char from the string rather than whole word.

print(str3.replace('v','b'))

#4. std.find(word): returns 1st index of 1st occurrer

str4 = "I have my own youtube channel"
print(str4.find('o'))

#we can also find the whole string

print(str4.find('youtube'))

#if we will try to find the word which does not exist in the string so it will return -1

print(str4.find('d'))

#5. str.count: returns the count of the word which is used in the string

print(str4.count('o')) #we can also count whole word rather than string
