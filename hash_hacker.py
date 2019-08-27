#! python3

""" This will take a known hash and with a loop, it will cycle through a list
of words, hashing each one and compare it to the known hash.
Then it will give you the password

I'm aware of a couple tools I could use, also there are
existing word lists out there but I am
afraid to use those as I dont want to accidentally upload malicious code...

This only hashes for one hash algorithm. That is a weakness in my program.
I wonder if it's possible to figure out what alogrith was used,
or to try multiple algortithms...
"""

import hashlib
import json


# Loops through a list of words and hashes each word to compare against a stolen hash
def hash_hacker(password_list, captured_hash):
    loop = 0
    for word in password_list:
        word_hash = hashlib.sha256(word.encode()).hexdigest()
        
        if word_hash == captured_hash:
            print('Success!\nThe password is:\n{}'.format(word))
            break
        else:
            loop += 1
            continue
        
    if loop == len(password_list):
        print('The password is not contained in this list')


# Takes user input to upload a json formated password list        
pass_list = input('What password list file do you want to use?\n')
with open(pass_list) as word_list:
    password_list = json.load(word_list)

# User input to paste a captured hash    
captured_hash = input('Enter the hash:\n')

hash_hacker(password_list, captured_hash)

# Currently this is a tremendous success! yay hacking tool #2
