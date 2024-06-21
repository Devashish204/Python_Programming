#Form a file containig numbers seperated by comma, print the count of even numbers.

'''with open("numbers.txt","w") as f:
    f.write("1,2,3,4,5,6,7,8,9,10")'''

with open("numbers.txt","r") as f:
    data = f.read()
    print(data)
    
    '''num = ""
    for i in range (len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num +=data[i]  '''

nums = data.split(",")
for val in nums:
    if(int(val)%2==0):
        count =+1

print(count) 
