def decor(func1):                            # Defining the Decorator
    def execute(*args,**kwargs):             # args and kwargs are needed if any function have arguments
        print("Fumction is executing.....")
        func1(*args,**kwargs)
        print("Function succesfully executed.")
    return execute

@decor           # Decorator
def name():
    print("My name is ZAID")

@decor           # Decorator
def add(a,b):
    print(a+b)

name()
add(10,20)