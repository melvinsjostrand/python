import random
print("Random characters from the Runes category:")

for _ in range(5):

    print(chr(random.randint(0x16A0, 0x16FF)), end=" ")
