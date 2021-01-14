# Lambda Function

def calculate(a,b):
    return a*a + 2*a*b + b*b

ans = calculate(2,3)
print(ans)

print((lambda a,b : a*a + 2*a*b + b*b) (4,3))

# OR

ans = (lambda a,b : a*a + 2*a*b + b*b) (5,3)
print(ans)