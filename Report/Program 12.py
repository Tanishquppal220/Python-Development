import random


def generate_password(length):
    all_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


length = int(input("Enter the length of the password: "))
password = generate_password(length)
print("Generated password:", password)
