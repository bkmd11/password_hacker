#! python3

""" A very shitty word list generator that I can feel comfortable
running in my own programs.

It is probably a waste of my time, but its good practice to write programs.

Ideas for methods of making the list:
Make all of these go through user_swap.main_user_swap so that I get every iteration
        Could make this a special flag once I set this up to argparse
Swap/add numbers into words


"""
import argparse

from password_hacker.word_list_generator import user_swap
from password_hacker.word_list_generator import user_input
from password_hacker.word_list_generator import known_keys
from password_hacker.word_list_generator import random_generator
from password_hacker.word_list_generator import file_writing


def main():
    parser = argparse.ArgumentParser(description='An attempt at being creative with word list generators')
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-uI', '--user_input', action='store_true',
                       help='Takes user input to generate a very simple list')
    group.add_argument('-rG', '--random_generate', type=int, metavar='int',
                       help='Randomly generates a set length of characters')
    group.add_argument('-kK', '--known_keys', type=str, metavar='ex. abc',
                       help='Takes known keys to iterate a list')
    parser.add_argument('-uS', '--user_swap', action='store_true',
                        help='Swaps each letter for a capitol')

    args = parser.parse_args()

    if args.user_input:
        word_list = user_input.user_input()
        if args.user_swap:
            word_list = user_swap.main_user_swap(word_list)
            file_writing.dump_json(word_list)
        else:
            file_writing.dump_json(word_list)
    elif args.random_generate:
        word_list = random_generator.random_generator(args.random_generate)
        if args.user_swap:
            word_list = user_swap.main_user_swap(word_list)
            file_writing.dump_json(word_list)
        else:
            file_writing.dump_json(word_list)
    elif args.known_keys:
        word_list = known_keys.known_keys(args.known_keys)
        if args.user_swap:
            word_list = user_swap.main_user_swap(word_list)
            file_writing.dump_json(word_list)
        else:
            file_writing.dump_json(word_list)


if __name__ == '__main__':
    main()

