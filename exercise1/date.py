date = input("Enter an american date: ")

while len(date) != 8:
    date = input("Enter an american date: ")

print(f"{date[6:8]}/{date[0:2]}/{date[3:5]}")