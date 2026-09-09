n = int(input("Enter a number: "))
p = int(input("Enter the position of the bit to check: "))
k = p
while k > 0:
    n >>= 1
    k -= 1
if n & 1:
    print(f"The {p}th bit is set.")
else:
    print(f"The {p}th bit is not set.")