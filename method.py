# Method in python

class student():
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll} , GPA : {self.gpa}")


rahim = student(101,3.57)  # An Object Of Student Class
rahim.display()

karim = student(102,3.75)
karim.display()
