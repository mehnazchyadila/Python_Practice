# Class & Object in python

class student():
    roll = ""
    gpa = ""



rahim = student()  # An Object Of Student Class
print(isinstance(rahim ,student))
rahim.roll = 101
rahim.gpa = 3.50
print(f"Rahim's Roll: {rahim.roll} , Rahim's GPA : {rahim.gpa}")

karim = student()
print(isinstance(karim ,student))
karim.roll = 102
karim.gpa = 3.57
print(f"karim's Roll: {karim.roll} , karim's GPA : {karim.gpa}")








