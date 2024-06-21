f = open("demo.txt","r")#if demo.txt was not in same folder than we need to
#mention complete path.

#data = f.read()
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
#print(data)
#print(type(data))
f.close()