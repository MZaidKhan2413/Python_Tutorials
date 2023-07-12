class A:
    def showA(self):
        print("This is class A")
class B(A):                      # Single Inheritance
    def showB(self):
        print("This is class B")
class C(B):                      # Multiple Inheritance
    def showC(self):
        print("This is class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()