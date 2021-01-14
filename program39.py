"""
List Comprehention
Formula
[Expression for item in List

"""
num = [1,2,3,4,5]

ans = list(filter(lambda x: x%2 == 0 ,num))

print(ans)


ans = [x for x in num if x%2 == 0]

print(ans)




