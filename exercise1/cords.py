import math

x1 = int(input("Enter the x-coordinate of the first point (x1): "))
y1 = int(input("Enter the y-coordinate of the first point (y1): "))
x2 = int(input("Enter the x-coordinate of the second point (x2): ")) 
y2 = int(input("Enter the y-coordinate of the second point (y2): "))

first_cord = x1,y1
second_cord = x2, y2
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(first_cord , second_cord , d)