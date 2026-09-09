import random


total = 0

for i in range(10):
    number = random.randint(1,10)
    print(number, end=" ")
    if(number % 2 != 0):
        total += number
print()
print("total is",total)