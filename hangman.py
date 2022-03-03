import sys
import random


def open_file_and_add_to_list(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            list = []
            for line in file:
                list.append(line.strip())
        return list
    except FileNotFoundError:
        print("file not found")


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    print("Użyte litery:", used_letters)
    print()


###
no_of_tries = 0
level = ""
path = "YOUR PATH TO FILE"
words = open_file_and_add_to_list(path)
word = random.choice(words)
used_letters = []
user_word = []
###

for _ in word:
    user_word.append("_")

print("""Choose level:
1 - easy
2 - normal
""")

if level == "1":
    no_of_tries = 8
else:
    no_of_tries = 5

while True:
    letter = input("Enter the letter: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("There is no such letter!")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("Game Over :(")
            print("It is a word to be guessed:", word.capitalize())
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Bravo, that's the word!")
            sys.exit(0)

    show_state_of_game()
