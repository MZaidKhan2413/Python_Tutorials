class Demo :
    name = ""
    age = 0
    
    def info(self):                          # Self keyword access the object of  this class
        print(f"The age of {self.name} is {self.age}")

obj = Demo()    # Object of class Demo
obj.name = "Zaid"
obj.age = 21
obj.info()
