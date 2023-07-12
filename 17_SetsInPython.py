'''
    Sets are the collection of UNORDERED datas !
    It is also same as list but set will IGNORES similars data present in it (Better understand with program 1)
    Output will not depend on the order of data present in a Set
'''
# Program 1 :
set1 = {10,20,20,20,30,40,50}         # First 20 will be read and other will be ignored !
print(set1)                           # Output : {50,20,40,10,30} (Not depending on order !)

# Set Methods :
set2 = {10,60,100,50}
set3= set1.union(set2)                # Set3 will contain all elements of 1&2
print(set3)

set3=set1.difference(set2)            # Contains the value which are common in 1&2 sets 
print(set3)

set3=set1.symmetric_difference(set2)  # Contains the value which are not common in 1&2 sets 
print(set3)

set1.update(set2)                     # set1 will now contains elements of set2 permanently !
print(set1)

# and many more (Some are similar to other datatypes).......