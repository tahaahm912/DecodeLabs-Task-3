import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special = "!@#"

    characters = letters + digits + special

    password = ""
    i = 0

    while i < length:
        password = password + random.choice(characters)
        i = i + 1

    return password


length = int(input("Enter password length: "))

if length < 4:
    print("Password should be at least 4 characters long.")
else:
    password = generate_password(length)
    print("Generated Password:", password)