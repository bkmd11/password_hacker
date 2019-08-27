""" Works like crunch sort of, but very random and needs work
 to make it actually useful
 """

import string
import random


def random_generator(n):
    random_list = []
    while len(random_list) <= 10000:
        all_letters = list(string.ascii_letters + string.digits)
        word = []
        for i in range(n):
            character = random.choice(all_letters)
            word.append(character)

        password = ''.join(word)
        random_list.append(password)
    return random_list
