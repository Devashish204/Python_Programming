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

#1. myDict_keys() :Returns all keys

print(info.keys())

#2. myDict.values() :Returns all values

print(info.values())

#3.myDict.items returns all (keys,val) pairs as tuples

print(info.items())

#4.myDict.get("Key") returns the key according to value

print(info.get("Name")) 

#5. myDic_update(new_dic) inserts the specified items to the direction.
new_dic = {"City":"Pune"}
info.update(new_dic)
print(info)