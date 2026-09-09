import time

if time.localtime().tm_hour < 10:
    print("Good morning!")
elif time.localtime().tm_hour < 16:
    print("Good afternoon!")
elif time.localtime().tm_hour < 17:
    print("Good evening!")
else:
    print("Good night!")