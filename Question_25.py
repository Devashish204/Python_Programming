#write a program to print the elements of the list in a single line.

num = [12,75,32,12]

def print_ele(list):
    list_size = len(list)
    i = 0
    while i < list_size:
        print(list[i],"\n") 
        i+= 1

print_ele(num)