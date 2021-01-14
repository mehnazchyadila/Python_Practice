# Set
# Set don't take duplicate value

num1 = {1,2,3,4,5,5}
print(num1)

num2 = set([1,2,3,4,5,7])
num2.add(10)
num2.remove(10)
print(num2)
print(7 in num2)
print(4 not in num2)

# Use of Union,Intersection , Minus

print(num1 | num2) # Union
print(num1 & num2) # Intersection
print(num1 - num2) # Minus

