""" Manipulates user input to swap letters with numbers and capitolize words
 Currently only swaps case for each letter, I want it to replace letters for similar numbers too
 ex. e = 3
 Also replaces all instances of a given letter instead of just replacing a single letter...

 It would be useful to make this take a text file, or json file as input
"""


def user_swap(word):
    swap_list = []
    for letter in word:
        new_letter = letter.swapcase()
        new_word = word.replace(letter, new_letter)
        swap_list.append(new_word)

    return swap_list


# Makes my user swap list bigger
def swap_for_word_in_list(swap_list):
    big_list = []
    for word in swap_list:
        big_list += user_swap(word)

    return big_list


# Makes a list of all variations on case in a word
def main_user_swap(word_list):
    main_list = []
    count = 0
    while count <= len(word_list):
        main_list += swap_for_word_in_list(word_list)
        main_list = list(dict.fromkeys(main_list))    # This takes out doubles
        word_list = main_list
        count += 1

    return main_list
