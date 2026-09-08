city_one = str(input("Enter a city "))
city_two = str(input("Enter a city "))
city_three = str(input("Enter a city "))

if city_one > city_two :
    city_one , city_two = city_two , city_one
if city_one > city_three : 
    city_one , city_three = city_three , city_one
if city_two > city_three :
    city_two, city_three = city_three , city_two

print(city_one , city_two, city_three)