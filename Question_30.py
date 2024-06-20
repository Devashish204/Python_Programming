#Write a recursive function to print all elements in the list.

def print_list(list,index=0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list,index+1)

num = [12,14,21,45,32]

print_list(num)