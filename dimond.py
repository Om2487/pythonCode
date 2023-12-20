class A:
    def method(self):
        print("This method belong to class A")
    pass
class B(A):
    def method(self):
        print("This method belong to B")
class C(A):
    def method(self):
        print("This method belong to C")

class D(B,C):
    pass

d=D()
d.method()

