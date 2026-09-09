char = input("Enter one character: ")
str = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
if char.lower() in str:
    if char.upper() == char:
        print("input character is uppercase letter")
    else: 
        print("input character is lowercase letter")
elif char in num:
        print("input character is number")
else:
    print("input character is a special character")
