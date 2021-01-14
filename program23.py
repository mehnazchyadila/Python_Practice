"""
n=3
*
* *
* * *
"""
n = int(input("Entre The Value Of N =  "))

for i in range(1,n+1,1):
    print(i * "*")

"""
n=3
*
* * *
* * * * *
"""
n= int(input("Enter The Value Of N = "))

for i in range(1,n+1,2):
    print(i * " *")

"""
n=3
      *
    * *
  * * * 
* * * *
"""
n = int(input("Enter The Value Of N = "))

for i in range(n , 1, 1):
    print(i * " *")
