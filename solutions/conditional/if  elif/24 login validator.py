data_base = {
    'aqheel' : "1234",
    'ali' : "1234",
    'ayesha' : "1234",
}

username = input("Enter your username: ")
if username in data_base:
    password = input("Enter your password: ")
    if password == data_base[username]:
        print("Login successful!")
    else:
        print("Incorrect password!")
else:
    print("Username not found!")