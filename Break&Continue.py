# Break & Continue Statement

# Break Statement
print("Break Statement ")
i=1
while i<=100:
    if i==20:
        break                                                       #When Loop get break statement it breaks the program
    print(i)
    i=i+1

# Continue Statement
print(" Continue Statement")
i=1
while i<=100:
    print(i)
    i=i+1
    if i==20:                                            # When Loop get Continue statement It sends it back to the loop
       continue

