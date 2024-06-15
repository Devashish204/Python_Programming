#1. set.add(el) adds an element
collection = set()
collection.add(1)
collection.add(2)
print(collection) 

#2. set.remove(el) removes an element
collection.remove(2)
print(collection)

#3. set.clear() empties the set
collection.clear()
print(collection)

#4. set.pop() removes a random value
set = {1,2,34}
set.pop()
print(set)

#5. set.union(set2) combines both set values and returns new
set2 = {5,2,56}
print(set.union(set2))

#6. set.intersection(set2) combines common values and return new
print(set.intersection(set2))
