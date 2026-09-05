print('############# MENU ##################')
print('# A) Triangle with * #')
print('# B) Largest K #')
print('# C) float list #')
print('# D#')
print('#####################################')




choice = input("Pick a math solution between A-D ").lower()
nmb_1 = float(input("Pick your first number: "))
nmb_2 = float(input("Pick your second number: "))

match choice:
    case 'a':
        result = nmb_2 * nmb_1
        print(result)
    case "b":
        result = nmb_1 / nmb_2
        print(result)
    case "c":
        result = nmb_1 - nmb_2
        print(result)
    case "d":
        result = nmb_1 + nmb_2
        print(result)
    

