#! /usr/bin/env python3

import sys
from operator import itemgetter

word_count = 0
current_word = None
word = None

# Read line from STDIN
for line in sys.stdin:
    # Remove whitespaces and new line from input
    l = line.strip()
    l = line.strip("\n")
    # Split each line into word and count 
    word, count = l.split("\t", 1)
    # Convert count to integer
    count = int(count) 
    
    # Increment the word_count if the current_word matches the word
    # Input is sorted based on alphabetical order
    if current_word == word:
        word_count += count
    else:
        # Print current_word and its count
        if current_word != None:
            print(f"{current_word}\t{word_count}")
        # Set current_word as the next word and initialise word_count to 1
        current_word = word 
        word_count = 1
# Required to print the last word and its count of the corpus
if current_word == word:
    print(f"{current_word}\t{word_count}")
