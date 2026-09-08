integers = []
integer = int(input("Insert an integer: "))

while integer > 0:
    integers.append(integer)
    integer = int(input("Insert an integer: "))

string_integers = ','.join(map(str, integers))

print(string_integers)