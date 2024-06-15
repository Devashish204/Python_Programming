marks = [85,94,76,63,48]
print(marks[1:4]) #last index is not included.

print(marks[:4]) #if we miss to mention the starting index 
#than it will consider it as 0th index.

print(marks[1:]) #if we miss to mention ending index than it
#will consider it as marks[0:len(marks)] means last or nth index
#of the list.

print(marks[-3:-1]) #list also supports negative slicing as it slice the list
# in reverse or negative order. 
