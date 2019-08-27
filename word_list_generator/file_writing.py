import json


# Writes the list to a json file
def dump_json(word_list):
    file_name = input('Enter the file name you want this saved as: ')
    with open('{}.json'.format(file_name), 'w') as pass_list:
        json.dump(word_list, pass_list)