value = int(input())

if(value < 0):
    print("Negative")
else:
    if(value % 2 == 0):
        print("Even")
    elif(value % 7 == 0):
        print("Divisible by 7")
    else:
        print("Odd")
