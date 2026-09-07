import random

count = [0] * 13
c = int(input("how many times do i roll the two dices: "))
for _ in range(c):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2

    count[total] += 1

for total in range(2,13):
    print(total, count[total])