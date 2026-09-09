n = int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print(f'{n} is divisible by both 3 and 5')
elif n%3==0:
    print(f'{n} is divisible by 3 only')
elif n%5==0:
    print(f'{n} is divisible by 5 only')
else:
    print(f'{n} is not divisible by neither 3 nor 5')