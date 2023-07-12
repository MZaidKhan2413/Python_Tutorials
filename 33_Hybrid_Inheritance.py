class A:
    def ShowA(self):
        print("This is class A")
class B(A):
    def ShowB(self):
        print("This is class B")
class C(B):
    def ShowC():
        print("This is class C")
class D(C):
    def ShowD(self):
        print("This is class D")
class E(C):
    def ShowE(self):
        print("This is class E")

# In above definations Class C is inherited by class A with Multilevel Inheritance and class D & E are inherited by class C with Heirrachical Inheritance
# So it produced HYBRID INHERITANCE

obj = D()
obj.ShowA()