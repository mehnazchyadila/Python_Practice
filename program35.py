# XXargs  work as dictionary

def student(**details):
    print(details)


student(id = 123,name ="Adila",GPA =3.50)

def student(**details):
    print(details["id"])


student(id = 123,name = "Adila",GPA = 3.50)
student(id = 124,name = "Afifa",GPA = 3.50)
student(id = 125,name = "Raisa",GPA = 3.50)

