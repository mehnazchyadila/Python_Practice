"""Types Of Inheritance"""

# Multi - Level Inheritance
print("Multi-Level Inheritance")
class A():
    def display1(self):
        print("This is inside A class")

class B(A):
    # display1
    def display2(self):
        print("This is inside B class")


class C(B):
    # display1
    # display2
    def display3(self):
        super().display1()
        super().display2()
        print("This is inside C class")

ob1 = C()
ob1.display3()

print("Multiple Inheritance")

# Multiple Inheritance

class A():
    def display1(self):
        print("This is inside A class")

class B():
    # display1
    def display2(self):
        print("This is inside B class")


class C(A,B):
    # display1
    # display2
    def display3(self):
        super().display1()
        super().display2()
        print("This is inside C class")

ob1 = C()
ob1.display3()

