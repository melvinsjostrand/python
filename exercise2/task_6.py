n = int(input("Enter an positive integer: "))

def sum_of_digits(n):
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    print(total)
    
if(n <= 0):
    n = int(input("Enter an positive integer: "))
else:
    sum_of_digits(n)