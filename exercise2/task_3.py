N = int(input())
total = 0
k = 1
while total + k > N:
    total += k
    k += 2

print(total)