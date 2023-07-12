'''List Comprehension :
                       These are used to create new lists from iterables like - 
                       list, tuples, dictionaries, sets, and even in Arrays & Strings.
    SYNTAX :
    List = [Expression(item) for item in Iterable if Condition]
    ~Expressioon :- It is the item which is being iterated;
    ~Iterable    :- It can be list, tuples, dictionaries, sets, and even in Arrays & String
    ~Condition   :- It checks if the items should be added in new list or not
'''

# Example 1 :
Lst=[i for i in range(1,10) if i%2==0]
print(Lst)

# Example 2 :
name = ["Zaid", "Junaid", "Rehan", "falak","Aina", "Ayan"]
NewName = [item for item in name if "i" in item ]
print(NewName)

# Example 3 :
strg = input("Enter a String : ")
print("With spaces :")
strlist = [char for char in strg]
print(strlist)

print("Withoout spaces :")
strlist = [char for char in strg if " " not in char]
print(strlist)