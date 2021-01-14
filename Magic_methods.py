 # Magic methods

"""
__eq__(self,other)    ==
__lt__(self,other)    <
__le__(self,other)    <=
__gt__(self,other)    >
__ge__(self,other)    >=
__ne__(self,other)    !=
__init__(self)
__str__(self)
__add__(self,other)
__sub__(self,other)
__mul__(self,other)
__div__(self,other)

"""

class Bike:
     def __init__(self,name,color):
        self.name = name
        self.color = color

     def __str__(self):
         return (f"Name : {self.name} , Color : {self.color}")

     def __eq__(self, other):
         return self.name == other.name and self.color == other.color

bike1 = Bike("Yamaha R15","White")
print(str(bike1))


bike2 = Bike("Yamaha RZ","Black")
print(str(bike2))




