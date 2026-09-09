integer = int(input("Enter a positive integer: "))

print("Using for: ", end=" ")
for i in range(1, integer + 1 ,2 ):
    print(i , end=" ")
print()
i = 1


print("Using while:", end=" ")
while i <= integer:
    print(i, end=" ")
    i += 2

