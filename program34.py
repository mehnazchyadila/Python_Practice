# Xargs

def student(id,name):
    print(id,name)

student(123,"Adila")

# Using Xargs we can work with many argument

def student(*details):
    print(details)


student(123,"Adila",3.50)

def student(*details):
    print(details[0])


student(123,"Adila",3.50)

def add(*numbers):
    sum = 0
    for num in numbers:
       sum = sum + num
       print(sum)

add(10,20)