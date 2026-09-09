vowels = 'AEIOU'
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

char = input("Enter a character: ")
if char.upper() in chars:
    if char.upper() in vowels:
        print(f'{char} is a vowel')
    else:
        print(f'{char} is a consonant')
else:
    print("given character is not an alphabet")