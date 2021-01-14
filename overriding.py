"""
Method Overriding

"""
class Phone():
    def __init__(self):
        print("I am in Super Class OR Phone Class")


class Symphony(Phone):
     def __init__(self):
        super().__init__()
        print("I am in Symphony Class")

s = Symphony()


