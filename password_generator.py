import random
import string


def gen_passwd(size, chars):
    return "".join(random.sample(chars, size))


chars = string.ascii_letters + string.digits + string.punctuation

size = int(input("How many letters should the password have? "))

print("Your password: ", gen_passwd(size, chars))
