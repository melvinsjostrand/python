import random

r = random.randint(-100, 100)
print("the number is ", r)

if(r > 0):
    if(r % 2 == 0):
        print("the number is even and positive")
    else:
        print("The number is odd and positive")
else:
    if(r % 2 == 0):
        print("The number is even and negative")
    else:
        print("The number is odd and negative")