# Count NumberOfWord,NumberOfLetter,NumberOfDigit


list = input("Enter A text ")

NumberOfWord = 0
NumberOfLetter = 0
NumberOfDigit = 0

for num in list:
    num = num.lower()
    if num>='a' and num <='z':
        NumberOfLetter = NumberOfLetter +1
    if num >= '0' and num <= '9':
        NumberOfDigit = NumberOfDigit + 1
    if num == " " :
        NumberOfWord = NumberOfWord + 1

print("NumberOfWord = ",NumberOfWord + 1)
print("NumberOfLetter = ",NumberOfLetter)
print("NumberOfDigit = ",NumberOfDigit)