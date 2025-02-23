import random

chars = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ!@£$%^&*().,?01234356789'

print("Enter number of password u want to create: ")
number = int(input())
print("Enter lenght of the password u want create: ")
length = int(input())

#symbols between 35 - 122
for x in range(number):
    for y in range(length):
        print(random.choice(chars),end="")
    print("")
