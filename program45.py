"""
Exception Handling

"""
try:
 num1 = int(input("Enter Any Integer number : "))
 num2 = int(input("Enter any integer number : "))
 result = num1 / num2
 print(result)

except (ValueError,ZeroDivisionError,IndexError):
           print("You have to insert any integer number ")

finally:
    print("Thanks")

def voter(age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote "

print(voter(19))
try:

  print(voter(17))
except ValueError as e:
    print(e)








