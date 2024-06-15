info = {
    "Key":"value",
    "Name":"Devashish",
    "College":"MIT-WPU",
    "Age":20,
    "isAdult":True,
    "Marks" : 94.4,
    "mylist" : ["Python","Java","C"],
    "Tuples" : ("Dict","Sets")
}

print(info)
print(type(info))

print(info["Name"])#we can access the element we wanted to
print(info["Age"])

#we can also change the value of the key as key is  mutable 

info["Name"] = "Dev"
print(info["Name"])

#and we can also add a new key:value pair in the dict.

info["Surname"] = "Rajput"
print(info)
print(info["Surname"])
