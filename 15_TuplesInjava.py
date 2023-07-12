'''
    Tuples are immutable Lists !
'''
tup1 = (10,20,30,"xyz",True,5.0)   # It is a tuple
tup2 = [10,20,30,"xyz",True,5.0]   # It is a List
print(type(tup1))
print(type(tup2))
print(tup1)

# operations in Tuple :
'''
    unlike list we cannot change or mutate tuples !
    To do operations in tuple, we convert tuples into a list and then perform opertaions
    after that we agian convert it into tuple !!
'''
# Example :
tup3 = (5,1,4,2,0)
print(tup3)
temp = list(tup3)
temp.append(9)
temp.sort()
tup3 = tuple(temp)
print(tup3)