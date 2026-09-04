a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))
c = int(input("Enter value for C: "))

if a == b or a == c or b == c:
    print("We have duplicate values.")
else:
    print("All values are unique.")