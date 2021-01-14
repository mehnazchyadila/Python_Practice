# Guessing Game
import random

guessnumber = int(input("Guess Number : "))

randomnumber = random.randint(1,5)

if guessnumber == randomnumber:
    print("You Won ")
else:
    print("You Loss ")
    print(randomnumber)
