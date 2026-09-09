m = int(input("Enter your age: "))
if m < 12:
    person = 'child'
elif m < 18:
    person = 'teenager'
elif m < 60:
    person = 'adult'
else:
    person = 'senior'

print(f'You are a {person}')