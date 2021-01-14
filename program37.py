# Map Function
# it works with a list and a function
# We also use here lambda function

number = [1,2,3,4,5]

def square(x):
    return x*x



answer = list(map(square,number))
print(answer)