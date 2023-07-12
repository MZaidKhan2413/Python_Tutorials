'''map(func,iterable) : It returns a map object which can be typcasted in any dataType'''
# Progam to understand map :

def cube(x):
    return x**3

list1 = [1,2,3,4,5]
newlist1 = map(cube,list1)
newlist1 = list(newlist1)
print(newlist1)

# newlist1 = list(map(lambda x:x*x,list1))      # square using lambda function
# print(newlist1)

'''filter(func,iterable) : It returns a filter object which can be typcasted in any dataType
the func argument will return a boolean value and filter fuction filter only true returned values !'''

# def func(a):
#     return a<=5

# list2 = [1,3,5,7,9]
# newlist2 = filter(func,list2)
# newlist2 = list(newlist2)
# print(newlist2)