"""
   Inheritance
 Before Inheritance

"""

class phone():
    def call(self):
        print("You can call")

    def message(self):
        print("You can Message")


class symphony():
    def call(self):
        print("You can call")

    def message(self):
        print("You can Message")

    def photo(self):
        print("You can take photo")


p = phone()
p.call()
p.message()

s = symphony()
s.call()
s.message()
s.photo()

"""
Parent class ,Super class ,Base class

"""
class phone():
    def call(self):
        print("You can call")

    def message(self):
        print("You can Message")

"""
Sub Class , Child Class , Derived Class 

"""
class symphony(phone):
    def photo(self):
        print("You can take photo")


p = phone()
p.call()
p.message()

s = symphony()
s.call()
s.message()
s.photo()
