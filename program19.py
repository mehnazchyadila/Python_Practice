# Some function

subjects =["C" , "C++" ,"Java" ,"Basic"]
length = len(subjects)
print(length)

#print(len(subjects))
subjects.append("TOC")
print(subjects)

subjects.insert(2,"Python")
print(subjects)

subjects.remove("C++")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()
print(subjects)

subjects.pop()
print(subjects)

subjects.clear()
print(subjects)

subjects3 = [1,23,43,65,2]
pos = subjects3.index(23)
print(pos)

subjects1 = subjects.copy()
print(subjects1)

subjects2 = ["C" , "C++" , "C++" ,"Java" ," C++"]
On_Of_Java = subjects2.count("C++")
print(On_Of_Java)






