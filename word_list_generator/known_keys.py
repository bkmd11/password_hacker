""" Takes a set of known keys and makes every possible combination
again, it can make a file that can be put into user swap
"""

import itertools


def known_keys(captured_keys):
    known_list = [''.join(i) for i in itertools.product(captured_keys, repeat = len(captured_keys))]
    return known_list

