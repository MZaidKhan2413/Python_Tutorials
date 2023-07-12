class A:
    def ShowA(self):
        print("This is class A")

# HEIRARCHICAL INHETRITANCE :-
class B(A):
    def ShowB(self):
        print("This is class B")
class C(A):
    def ShowC(self):
        print("This is class C")

obj1 = C()
obj1.ShowA()
obj1.ShowC()
# obj1.ShowB()    # This will throw an error because class C is not inherited by class B

obj2 = B()
obj2.ShowA()
obj2.ShowB()