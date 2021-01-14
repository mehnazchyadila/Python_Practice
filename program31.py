# Queue

from collections import deque
bank = deque(["Adila","Ethia","Rodela"])

print(bank)

bank.popleft()
print(bank)
bank.popleft()
print(bank)

bank.popleft()
print(bank)

if not bank:
    print("No person left")