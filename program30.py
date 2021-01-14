# Stack [LIFO = Last in Fast Out]

books = []
# Push the Item
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
books.append("Learn Python")

print(books)

# Pop The Item

books.pop()
print(books)
print("Now The Top Book Is ",books[-1])

books.pop()
print(books)
print("Now The Top Book Is ",books[-1])

books.pop()
print(books)
print("Now The Top Book Is ",books[-1])

books.pop()
if not books:
    print("No Books Left ")





