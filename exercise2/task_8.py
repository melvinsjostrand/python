text = input("Enter a sentence: ")





def reverse_words(text):
    txt = text.split(" ")
    txt.reverse()
    print("Reversed text: " , " ".join(txt))

def count_vowels(text):
    vowels = set('aeiouAEIOU')
    vowels_amount = 0
    for char in text:
        if char in vowels:
            vowels_amount += 1
    print(vowels_amount)

def find_longest_word(text):
    txt = [len(word) for word in text.split()]
    
    print(txt)
def is_palindrome(text):    
    print()


reverse_words(text)
count_vowels(text)
find_longest_word(text)