#list as user input

n = input("Enter a text of number : ")
list = n.split()

sum = 0

for n in list:
    sum = sum + int(n)
print(sum)


