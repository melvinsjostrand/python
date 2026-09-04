print('############# MENU ##################')
print('# a) Math-program #')
print('# b) Text-editor #')
print('# c) Games #')
print('# #')
print('#####################################')
choice = input('Enter your choice (a-c):').lower()
match choice:
    case 'a':
        print("a")
    case 'b':
        print("b")
  
    case 'c':
        print("c")
    case _:
        print("Invalid choice. Please select a valid option (a-c).")