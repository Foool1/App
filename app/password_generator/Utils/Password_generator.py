import random

def generate_password(length):
    chars = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ!@£$%^&*()?01234356789'

    password = ''
    if length<4: return 'password to short'
    elif length>32: return 'password to long'
    for y in range(length):
        password += random.choice(chars)
    return password
