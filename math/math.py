print('############# MENU ##################')
print('# a) Triangle with * #')
print('# b) Largest K #')
print('# c) float list #')
print('# #')
print('#####################################')


def positive_int():
    float_lst = [1.3, 2.67, -2.25, 4.88, 5.99, -6.01, 7.0, 8.5, -9.75]
    new_list = []

    for i in range(len(float_lst)):
        if(float_lst[i] > 0):
          new_list.append(float_lst[i])

    return(new_list)


def largest_K(N):
    total = 0
    K = 1

    while total + K < N:
        total += K
        K += 2

    return K - 2


choice = input('Enter your choice (a-c):').lower()
match choice:
    case 'a':
        N = int(input("input range: "))
        for _ in range():
            print("*" * _)
        

    case 'b':
        N = int(input("Give me a positive number: "))
        if(N < 0):
            print("need to be a pos number")
        else:
            print(largest_K(N))



  
    case 'c':
       print(positive_int())


    case _:
        print("Invalid choice. Please select a valid option (a-c).")
