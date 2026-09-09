n = int(input("Enter a number: "))
count = 0
m = n
while m:
    count += m & 1
    m >>= 1
print(f"Number of set bits in {n} is {count}")