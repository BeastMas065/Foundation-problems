print("Select input units \n1 for fahrenheit and 2 for Celsius")
n = int(input(""))
temp = float(input("Enter temperature: "))
match n:
    case 1:
        res = (temp -32) *5/9
        print(f'temp in Celsius is {res}')
    case 2:
        res = (temp)*9/5+32
        print(f'temp in Fahrenheit is {res}')
    case _:
        print("invalid input")
