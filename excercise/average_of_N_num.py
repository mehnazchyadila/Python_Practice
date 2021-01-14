# How to find average of N numbers in Python
n = int(input("Enter The value of N : "))
total_numbers = 0
for num in range(n):
    numbers = float(input("Numbers = "))
    total_numbers = total_numbers + numbers

average = total_numbers/n

print("Average is ",average)
