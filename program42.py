"""
File Reading
"""
file = open("student.txt","r")
print(file.readable())

text = file.read()
print(text)
size = len(text)
print(size)

file = open("student.txt","r")
text = file.readlines()
print(text)

file = open("student.txt","r")
for line in file:
    print(line)

file.close()