import random

pick = int(input("Enter your choice (0 for scissors, 1 for rock, 2 for paper): "))

computer = random.randint(0, 2)
print(computer)

if(pick == 0):
    print("You picked scissors")
elif(pick == 1):
    print("You picked rock")
else:
    print("You picked paper")

if(computer == 0):
    print("Computer picked scissors")
elif(computer == 1):
    print("Computer picked rock")
else:
    print("Computer picked paper")

if(computer == pick):
    print("draw")
elif(pick == 0 and computer == 2):
    print("you win")
elif(pick == 1 and computer == 0):
    print("you win")
elif(pick == 2 and computer == 1):
    print("you win")
else:
    print("you lose")
