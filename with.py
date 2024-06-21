#for right(r)
with open("demo.txt","r") as f:
   data = f.read()
   print(data)

#for write(w)
with open("demo.txt","w") as f:
   data = f.write("My name is Dev!")
   print(data)