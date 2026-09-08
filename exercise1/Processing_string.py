text = str(input("Enter a string: "))

space_count = text.count(" ")

print("Length:" , len(text))
print("Number of spaces:" , space_count)
print("First and last letter:", text[0], text[-1])

if "python" in text.lower():
    print("Does it contain Python? Yes")
else:
    print("Does it contain Python? no")
