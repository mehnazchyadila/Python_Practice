# Filter Function is also work with a list and a named or lambda (anonymous) function
# It work as a filter

num = [1,2,3,4,5]

ans = list(filter(lambda x:x%2 == 0,num))

print(ans)