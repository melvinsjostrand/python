number_one = int(input("Enter a number "))
number_two = int(input("Enter a number "))
number_three = int(input("Enter a number "))

if number_one < number_two :
    number_one , number_two = number_two , number_one
if number_one < number_three : 
    number_one , number_three = number_three , number_one
if number_two < number_three :
    number_two, number_three = number_three , number_two

print(number_one , number_two, number_three)