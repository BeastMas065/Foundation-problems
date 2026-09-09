n = int(input("Enter a number: "))
if n>0:
    print(f'{n} stands on the right side (positive) of the number line')
else:
    print(f'{n} stands on the {"left side (negative)" if n<0 else "start (zero)"} of the number line')