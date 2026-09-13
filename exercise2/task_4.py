n = int(input())

print("Right-Angled Triangle:")
for i in range (n):
    print(" " * i, "*" * (n-i))

print("Isosceles Triangle:")
for i in range(n):
    print(" " * (n - i), "*" * (2*i+1))