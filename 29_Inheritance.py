class A:
    def show(self):
        print("This is class A's method")

class B(A):                              # Single inheritance
    def showB(self):
        print("This is class B's method")

obj1 = B()
obj1.show()
obj1.showB()

obj2 = A()
obj2.show()
# obj2.showB()     # ERROR