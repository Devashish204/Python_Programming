list = [2,1,3]

#list.append :adds one element at the end

list.append(4)
print(list)

#list.sort() :sorts list in ascending order

list.sort()
print(list)

#list.sort(reverse = true) :sorts list in descending order

list.sort(reverse= True)
print(list)

#list.insert(index,element) :insert element at index
list.insert(0,65)
print(list)#insert method not replace the value but it just 
#insert new element in the index and pushes other values which
#are next to in in +1 indexes.

#list.remove(1) :removes first occurrence of element

list2 = [2,1,3,1]

list2.remove(1)
print(list2)

#list.pop(index) :removes the element at index

list2.pop(0)
print(list2)