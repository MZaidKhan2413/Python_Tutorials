'''
    Dictionaries are the ordered collection of data items
    They store multiple items in a single variable
    Dictionary items are KEY-VALUE pairs seperated by commas & enclosed with {}
'''
# Example Program :
dic ={
    "Name":"Zaid",
    "Age" : 21,
    "Work": "Coding"
}

print(dic)
print(dic["Age"])              # If item is not in dictionary it will through ERROR !
print(dic.get("Name"))         # If item is not in dictionary it will give NONE
print(dic.keys())              # Print all keys of Dictionary
print(dic.values())            # Print all values of Dictionary
print(dic.items())             # Print all the items in Dic as list of tuples

# Iteration through Dictionary :
for i in dic:
    print(i)                   # Show the keys of Dictionary
    print(dic[i])              # Show the values correspoding to the keys

for i,j in dic.items():
    print(f"The value of {i} is {j}")

# Dictionary Methods are also similar (mostly) to other dataStructures in python !!