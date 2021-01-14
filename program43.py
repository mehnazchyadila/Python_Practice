# File Writing
"""
If we write [open("student.txt","w")] it overlap the existing text file .For this we write [open("student.txt","a")] .
It add the addition value with the existing file .

"""
file = open("student.txt","a")
file.write("Rista Chowdhury - Studied in class Nine")

file = open("student1.txt","a")
file.write("Rista Chowdhury - Studied in class Nine")

file = open("hello.html","a")
file.write("<h1>This file create a Html Page <h1\>")



file.close()