n = int(input("Enter a number:"))

if(n < 0):
    print(n, "Give me a positive number")
else:
    if(n % 4 == 0 and n % 3 ==0):
        print(n, "does not fulfill the condition")
    else:
        if(n % 4 == 0):
            print(n, "is divisible by 4")
        elif(n % 3 == 0):
            print(n, "is divisible by 3")
        else:
            print(n, "is not divisible by 3 or 4")