float_lst = [1.3, 2.67, -2.25, 4.88, 5.99, -6.01, 7.0, 8.5, -9.75]



def positive_int(float_lst):
    new_list = []

    for i in range(len(float_lst)):
        if(float_lst[i] > 0):
          new_list.append(float_lst[i])

    return(new_list)

print(positive_int(float_lst))

def largest_K(N):
    total = 0
    K = 1

    while total + K < N:
        total += K
        K += 2

    return K - 2

print(largest_K(40))


for _ in range(8):
    print("*" * _)

    