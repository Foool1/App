import random

def generate_password(length):
    chars = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ!@£$%^&*()?01234356789'

    password = ''

    for y in range(length):
        password += random.choice(chars)
    return password
