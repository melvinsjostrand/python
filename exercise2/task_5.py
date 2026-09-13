number = int(input("Give an integer: "))

zero = 0
odd = 0
even = 0

while number > 0:
    digit = number % 10

    if digit == 0:
        zero += 1
    elif digit % 2 == 0:
        even += 1
    elif digit % 2 != 0:
        odd += 1

    number = number // 10

print(f"""Zeros: {zero}
Even: {even}
Odd: {odd}""")