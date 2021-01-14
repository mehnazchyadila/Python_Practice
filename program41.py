"""
Recursion
It is a process where it can call itself.
To stop calling we need a base case.

2 important points in case of Recursion :
* Recursive Call
* Base case

"""

def fact(n):

    if (n == 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(4))