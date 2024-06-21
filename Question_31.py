#Create a new file "practical.txt" using python. Add  the following data in it.

f = open("practice.txt","w")
about = f.write("Hi everyone\nwe are learning File I/O\nusing python.\nI like programming in python.")
print(about)
f.close()

#Write a function that replace all occurences of "python" with "java" in above file.

f = open("practice.txt","r")
data = f.read()
new_data = data.replace("python","Java")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#search if the word "learning" exists in the file or not

with open("practice.txt","r") as f:
    data = f.read()
   
if( data.find("learning")!= -1):
    print("found")
else:
    print("not found")

   
