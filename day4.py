"""Day 4 of Advent of Code 2017"""

import utils

def get_input():
    """Get input4.txt data as list of strings"""
    input_text = utils.get_day_input(4)
    passphrase_list = input_text.splitlines()

    return passphrase_list


def puzzle_1(passphrase_list):
    """Puzzle 1 Solution"""
    num_valid = 0
    for line in passphrase_list:
        if no_repeating_words(line):
            num_valid = num_valid + 1

    return num_valid

def no_repeating_words(line):
    """Check if any words are repeated in line"""
    word_list = line.split(' ')
    word_set = set(word_list)

    return len(word_list) == len(word_set)

def puzzle_2(passphrase_list):
    """Puzzle 2 Solution"""
    num_valid = 0
    for line in passphrase_list:
        if no_anagrams(line):
            num_valid += 1

    return num_valid

def no_anagrams(line):
    """Check if any words are anagrams of any other words"""
    word_list = line.split(' ')
    sorted_word_list = [''.join(sorted(x)) for x in word_list]
    sorted_word_set = set(sorted_word_list)

    return len(word_list) == len(sorted_word_set)

if __name__ == '__main__':
    print(puzzle_1(get_input()))
    print(puzzle_2(get_input()))
