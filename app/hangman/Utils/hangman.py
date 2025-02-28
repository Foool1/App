import random
from words import words


def enter(word_list, word, live, used_letters):
    letter = input()
    used_letters.append(letter)
    counter = 0
    for x in range(len(word_list)):
        if letter == word[x]:
            word_list[x] = letter
            counter = counter + 1

    if counter == 0:

        return 0


def printing(word_list):
    for x in range(len(word_list)):
        print(word_list[x], end="")
        print(" ",end="")
    print("\n")


def winning(word_list):
    for x in range(len(word_list)):
        if word_list[x] == "_":
            return 0
    return 1

word = random.choice(words)
print(word)

live = 10


word_list = []
used_letters = []


for x in range (len(word)):
    word_list.append("_")

while live != 0:
    print("You have ", live, "lives left and you already used these letters: ",*used_letters)
    print("Guess the letter in the word:")

    printing(word_list)
    if enter(word_list, word, live, used_letters) == 0:
        print("You are wrong", end=", ")
        live = live - 1
    else:
        print("\nYou are correct", end=", ")

    if live == 0:
        print("You lose, try again")

    if winning(word_list) == 1:
        print(f"You won, the world is: {word}, congratulations!")
        live = 0
        break
