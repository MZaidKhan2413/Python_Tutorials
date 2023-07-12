'''lambda function is used to make one liner functions in a program.
When the fuction defination is very very short then we use it.
It is known as anonymous functon as we dont need to name it unless required'''

# Normal functiom :
def sum(a,b):
    return a+b

# lambda function :
sum1 = lambda a,b:a+b

print(sum(10,20))
print(sum1(5,15))