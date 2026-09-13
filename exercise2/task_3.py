N = int(input())
total = 0
k = 1

while total + k <= N:
    total += k
    k += 2
print(k, "is the smallest k such that 1+3+5+...+k >", N)

total = 0
k = 0
while total + k < N:
    total +=k
    k += 2
print(k - 2 , "is the largest k such that 0+2+4+6+...+k <" , N)



