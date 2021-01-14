from math import *

# 1+ 2 + 3 + ......+ n

n = int(input("Enter the Last Number  : "))

sum = 0

for i in range(1,n+1,1):
    sum = sum + i

print("Summation Of series : ",sum)

#Series Of Even number

n = int(input("Enter the Last Number  : "))

sum = 0

for i in range(2,n+1,2):
    sum = sum + i

print("2 + 4 + .....+ ",n)
print("Summation Of Even Number : ",sum)

#Series Of Odd number

n = int(input("Enter the Last Number  : "))

sum = 0

for i in range(1,n+1,2):
    sum = sum + i

print("1 + 3 + .....+ ",n)
print("Summation Of odd Number : ",sum)

#Series Of 4 + 8 + ..... + n

n = int(input("Enter the Last Number  : "))

sum = 0

for i in range(4,n+1,4):
    sum = sum + i

print("4 + 8 + .....+ ",n)
print("Summation Of Even Number : ",sum)


#Series Of 1^2 + 2^2 + ..... + n

n = int(input("Enter the Last Number  : "))

sum = 0

for i in range(1,n+1,1):
    sum = sum + pow(i,2)

print("1^2 + 2^2 + ..... + ",n)
print("Summation Of Even Number : ",sum)

#Series Of 2^2 + 4^2 + ..... + n

n = int(input("Enter the Last Number  : "))

sum = 0

for i in range(2,n+1,2):
    sum = sum + pow(i,2)

print("2^2 + 4^2 + .....  ",n)
print("Summation Of Even Number : ",sum)