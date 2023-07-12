'''Constructor in python are of 2 types :
1] Default
2] Parameterized
Constructor is initialized by __init__ function'''

class Demo :

    def __init__(self):                     #Default Constructor
        print("This is a Default constructor !")

    def __init__(self,name,age):            #Parameterized Constructor
        print(f"{name} is {age} years old")

# obj = Demo()  # Default constructor will automatically called

obj1 = Demo("Zaid",19)   # Parameterized constructor will be called