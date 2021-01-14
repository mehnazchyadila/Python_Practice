"""
Exception
Runtime Error / Incorrect input / Incorrect code
There are many kind of Exception
* TypeError
* ZeroDivisionError
* IndexError
* Value Error


"""

"""num1 = input("Enter any number : ")
result = 20 / num1 #TypeError Exception
print(result)
print("Done")"""

num1 = int(input("Enter any number : "))
result = 20 / num1
"""TypeError Exception & ZeroDivisionError if we divide it 0 """
print(result)
print("Done")

text = "Adila"
print(text[0])
"""print(text[5]) #IndexError"""
print("Done")

"""
For Handling exception we have to use try: - except:
 
"""
try:
    list = [20,0,30]
    result= list[0] / list[1]
    print(result)
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError :
    print("Dividing by Zero not possible")
except IndexError :
    print("Index Error")
except TypeError:
    print("descriptor '__init__' of 'super' object needs an argument == super()")
finally:
    print("Successful")