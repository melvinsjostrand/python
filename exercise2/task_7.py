

def triangle(x1,y1,x2,y2,x3,y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def slope(x1,y1,x2,y2):
    return ((y2 - y1) / (x2 - x1))

def midpoint(x1,y1,x2,y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x,y

while True:
    print("""Select a calculation:
    1. Slope of a line
    2. Midpoint of two points
    3. Area of a triangle
    0. Exit
    """)

    pick = int(input("Enter your choice (0-3): "))

    if(pick == 1):
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        result = slope(x1, y1, x2, y2)

        print(f"""
        The slope of the line through
        ({x1}, {y1}) and ({x2}, {y2}) is {result}.
        """)
    elif(pick == 2):
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        x,y =  midpoint(x1,y1,x2,y2) 

        print(f"""
        The midpoint between ({x1}, {y1})
        and ({x2}, {y2}) is ({x}, {y}) 
        """)
    elif(pick == 3):
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        x3 = float(input("Enter x3: "))
        y3 = float(input("Enter y3: "))

        result = triangle(x1,y1,x2,y2,x3,y3)

        print(f"""
        The area of the triangle with vertices
        ({x1}, {y1}), ({x2}, {y2})
        ({x3}, {y3}) is {result}
        """)
        
    elif(pick == 0):
        print("Exiting program")
