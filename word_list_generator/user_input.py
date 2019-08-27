""" Takes user input to generate a list of possible passwords
Not really a useful part of this tool, but it will eventually create a file that gets passed to
another function
"""


def user_input():
    user_list = []
    while True:
        word = input('Add a word to the list: ')
        if word == '':
            return user_list
        else:
            user_list.append(word)